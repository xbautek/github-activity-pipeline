from datetime import date, datetime, timezone
import logging
from pathlib import Path
import sys
import tempfile
from time import perf_counter
import urllib3
import argparse as ap

CHUNK_SIZE = 1024 * 1024

class ArchiveDownloader:
    BASE_URL = "https://data.gharchive.org"
    DATA_DIR = Path(__file__).resolve().parent.parent / "data"
    LOG_DIR = Path(__file__).resolve().parent.parent / "logs"

    def __init__(self, date: date, hour: int = None):
        self.date = date
        self.hour = hour
        self.http = urllib3.PoolManager()
        self.run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        log_date = datetime.now().date().isoformat()
        self.log_path = self.LOG_DIR / log_date / "application.log"
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger(f"archive_downloader.{self.run_id}")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s run_id=%(run_id)s %(message)s"
        )
        for handler in (logging.StreamHandler(sys.stdout), logging.FileHandler(self.log_path, mode="a", encoding="utf-8")):
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _log(self, message: str, level: int = logging.INFO) -> None:
        self.logger.log(level, message, extra={"run_id": self.run_id})

    def get_filename(self, hour: int = None) -> str:
        hour = self.hour if hour is None else hour
        if hour is None:
            return f"{self.date.isoformat()}.json.gz"
        return f"{self.date.isoformat()}-{hour}.json.gz"

    def get_url(self, hour: int = None) -> str:
        if hour is None:
            return f"{self.BASE_URL}/{self.get_filename()}"
        if hour not in range(24):
            raise ValueError(f"Invalid hour: {hour}")
        else:
            return f"{self.BASE_URL}/{self.get_filename(hour)}"

    def get_output_path(self) -> Path:
        return self.DATA_DIR / self.date.isoformat() / self.get_filename()

    def download(self) -> Path:
        output_path = self.get_output_path()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        incomplete_paths = list(output_path.parent.glob(f".{output_path.name}.*.part"))
        for incomplete_path in incomplete_paths:
            self._log(f"[INCOMPLETE] previous_partial={incomplete_path}")

        if self.check_if_file_exists():
            self._log(f"[COMPLETE] existing_file={output_path}")
            user_input = input("If you'd like to continue and replace file, write: Y, otherwise click any other key: ")

            if user_input.strip().upper() != "Y":
                self._log("[SKIPPED] existing_file_left_unchanged=true")
                raise RuntimeError("Download aborted by user.")
            self._log("[OVERWRITE_CONFIRMED] existing_file=true")

        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=output_path.parent, prefix=f".{output_path.name}.", suffix=".part", delete=False
            ) as output_file:
                temporary_path = Path(output_file.name)
                hours = range(24) if self.hour is None else (self.hour,)
                for hour in hours:
                    self._download_hour(output_file, hour)

            temporary_path.replace(output_path)
        except Exception:
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
            raise

        return output_path

    def _download_hour(self, output_file, hour: int) -> None:
        url = self.get_url(hour)
        started_at = perf_counter()
        byte_count = 0
        response = None
        try:
            response = self.http.request(
                "GET",
                url,
                preload_content=False,
                timeout=urllib3.Timeout(connect=5.0, read=60.0),
                retries=urllib3.Retry(total=3),
            )
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}")

            for chunk in response.stream(amt=CHUNK_SIZE):
                if chunk:
                    output_file.write(chunk)
                    byte_count += len(chunk)
        except Exception as error:
            elapsed = perf_counter() - started_at
            self._log(
                f"[FAILED] source_hour={hour} url={url} bytes={byte_count} duration={elapsed:.2f}s error={error}",
                logging.ERROR,
            )
            raise
        else:
            elapsed = perf_counter() - started_at
            self._log(f"[OK] source_hour={hour} result=downloaded bytes={byte_count} duration={elapsed:.2f}s")
        finally:
            if response is not None:
                response.release_conn()
# Napisz najprostsze testy jednostkowe klasy archivedownloader -> utwórz folder tests
    def run(self) -> Path:
        started_at = perf_counter()
        requested_hour = self.hour if self.hour is not None else "all"
        self._log(f"[RUN_STARTED] date={self.date.isoformat()} requested_hour={requested_hour}")
        try:
            output_path = self.download()
        except Exception as error:
            elapsed = perf_counter() - started_at
            self._log(f"[RUN_FAILED] duration={elapsed:.2f}s error={error}", logging.ERROR)
            raise

        elapsed = perf_counter() - started_at
        self._log(
            f"[RUN_COMPLETED] output={output_path} bytes={output_path.stat().st_size} duration={elapsed:.2f}s"
        )
        return output_path

    def check_if_file_exists(self) -> bool:
        return self.get_output_path().exists()

    @staticmethod
    def valid_hour(s: str) -> int:
        try:
            hour = int(s)
            if 0 <= hour <= 23:
                return hour
            else:
                raise ValueError
        except ValueError:
            raise ap.ArgumentTypeError(f"not a valid hour: {s!r}")


    @staticmethod
    def valid_date(s: str) -> date:
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            raise ap.ArgumentTypeError(f"not a valid date: {s!r}")