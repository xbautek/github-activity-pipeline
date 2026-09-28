import argparse as ap
from datetime import date, datetime
from pathlib import Path
import urllib3
from archivedownloader import ArchiveDownloader

parser = ap.ArgumentParser(description="Download script")
parser.add_argument("--date", type=ArchiveDownloader.valid_date, required=True, help="Date of the file to download")
parser.add_argument("--hour", type=ArchiveDownloader.valid_hour, required=False, help="Hour of the file to download")

args = parser.parse_args()


if __name__ == "__main__":
    downloader = ArchiveDownloader(args.date, args.hour)
    saved_path = downloader.run()
    print(f"Saved to {saved_path}")




