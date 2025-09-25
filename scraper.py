# scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    # Headlines may be inside h2 or h3 tags
    headlines = soup.find_all(["h2", "h3"])

    titles = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]
    return titles

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, title in enumerate(headlines, start=1):
            f.write(f"{i}. {title}\n")

def main():
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)

    if headlines:
        print(f"✅ Found {len(headlines)} headlines.")
        for h in headlines[:10]:
            print("-", h)
        save_to_file(headlines)
        print("✅ Headlines saved to headlines.txt")
    else:
        print("⚠️ No headlines found.")

if __name__ == "__main__":
    main()
