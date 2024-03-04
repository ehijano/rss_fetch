import subprocess
import datetime

def fetch_categories():
    return ['hep-th', 'cs.CV', 'cs.AI']  

def fetch_rss_for_categories(categories):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    for category in categories:
        filename = f"{date_str}_{category}.xml"
        url = f"https://rss.arxiv.org/rss/{category}"
        subprocess.run(['curl', url, '-o', filename], check=True)

if __name__ == "__main__":
    categories = fetch_categories()
    fetch_rss_for_categories(categories)