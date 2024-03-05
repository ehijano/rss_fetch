import requests
from bs4 import BeautifulSoup
import re
import json
from typing import Dict
import os

FOLDER = 'taxonomy_data'

def get_taxonomy():
    target_url = "https://arxiv.org/category_taxonomy"
    category_dictionary = {}

    try:
        response = requests.get(target_url)
        doc = BeautifulSoup(response.text, 'html.parser')
        category_info = doc.find_all('h4')
        
        for item in category_info[1:]:  # Starting from 1 to skip the first item, similar to the Java code
            content = item.text
            pattern = re.compile("(.*?) \\((.*?)\\)")
            matcher = pattern.finditer(content)
            for match in matcher:
                category = match.group(1)
                description = match.group(2)
                category_dictionary[category] = description
                
    except requests.exceptions.RequestException as e:
        print(e)
    
    return category_dictionary


def save_json(tax_dict:Dict[str,str])->None:
    base_workspace_path = os.getenv('GITHUB_WORKSPACE', '.')
    folder_path = os.path.join(base_workspace_path , FOLDER)
    path = os.path.join(folder_path, 'tax.json')


    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(path, 'w') as json_file:
        json.dump(tax_dict, json_file, indent=4)


if __name__ == "__main__":
    result = get_taxonomy()
    save_json(tax_dict=result)
    