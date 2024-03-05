import subprocess
import datetime
import os
import json

FOLDER = 'taxonomy_data'
URL = "https://rss.arxiv.org/rss"

def fetch_categories():

    base_workspace_path = os.getenv('GITHUB_WORKSPACE', '.')
    folder_path = os.path.join(base_workspace_path , FOLDER)
    path = os.path.join(folder_path, 'tax.json')

    if os.path.exists(path):
        with open(path, 'r') as json_file:
            taxonomy = json.load(json_file)
        return list(taxonomy.keys())
    else:
        return ['hep-th', 'cs.CV', 'cs.AI'] 

def fetch_rss_for_categories(categories):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    base_workspace_path = os.getenv('GITHUB_WORKSPACE', '.')

    base_path = os.path.join(base_workspace_path, "rss_data")
    os.makedirs(base_path, exist_ok=True)


    for category in categories:
        category_path = os.path.join(base_path, category)
        os.makedirs(category_path, exist_ok=True)

        filename = f"{date_str}_{category}.xml"
        file_path = os.path.join(category_path, filename)

        url = f"{URL}/{category}"
        subprocess.run(['curl', url, '-o', file_path], check=True)

if __name__ == "__main__":
    categories = fetch_categories()
    fetch_rss_for_categories(categories)