import csv
import time
from typing import List

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0 Safari/537.36"
}

def fetch_titles(pages: int = 1, delay: float = 1.0) -> List[str]:
    """
    Grab anime titles from MAL Top Anime.
    pages=1 -> first 50; pages=2 -> first 100 (etc.)
    """
    titles: List[str] = []

    for i in range(pages):
        url = f"https://myanimelist.net/topanime.php?limit={i*50}"
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Primary selector seen on MAL Top Anime
        anchors = soup.select("a.hoverinfo_trigger.fl-l.fs14.fw-b")
        # Fallback in case classes change slightly
        if not anchors:
            anchors = soup.select(".ranking-list .detail a[href*='/anime/']")

        titles.extend(a.get_text(strip=True) for a in anchors)
        time.sleep(delay)  # be polite

    # Drop duplicates while keeping order
    seen = set()
    uniq = []
    for t in titles:
        if t not in seen:
            uniq.append(t)
            seen.add(t)
    return uniq


def save_csv(titles: List[str], path: str = "anime_titles.csv") -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["title"])
        for t in titles:
            w.writerow([t])


if __name__ == "__main__":
    titles = fetch_titles(pages=1)  
    print(f"Collected {len(titles)} titles")
    save_csv(titles)
    print("Saved to anime_titles.csv")