import subprocess
import datetime
import os

def fetch_categories():
    return ['hep-th', 'cs.CV', 'cs.AI']  

def fetch_rss_for_categories(categories):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    base_workspace_path = os.getenv('GITHUB_WORKSPACE', '.')

    for category in categories:
        category_path = os.path.join(base_workspace_path, category)
        os.makedirs(category_path, exist_ok=True)

        filename = f"{date_str}_{category}.xml"
        file_path = os.path.join(category_path, filename)

        url = f"https://rss.arxiv.org/rss/{category}"
        subprocess.run(['curl', url, '-o', file_path], check=True)

if __name__ == "__main__":
    categories = fetch_categories()
    fetch_rss_for_categories(categories)