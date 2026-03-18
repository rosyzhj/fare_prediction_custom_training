#!/usr/bin/env python3
"""Extract yellow taxi parquet links from the NYC TLC trip data page."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

TLC_PAGE = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"


def extract_links(start_year: int, end_year: int) -> list[str]:
    resp = requests.get(TLC_PAGE, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    years = [str(y) for y in range(start_year, end_year + 1)]

    links: set[str] = set()
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        if "yellow_tripdata" not in href or ".parquet" not in href:
            continue
        if not any(year in href for year in years):
            continue
        links.add(urljoin(TLC_PAGE, href).strip())

    return sorted(links)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=2024)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/links/yellow_2024_2025_links.txt"),
        help="Output txt file with one parquet URL per line",
    )
    args = parser.parse_args()

    links = extract_links(args.start_year, args.end_year)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(links) + "\n", encoding="utf-8")

    print(f"Saved {len(links)} links to {args.output}")


if __name__ == "__main__":
    main()
