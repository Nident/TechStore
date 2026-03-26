import json 
from pprint import pprint

data_path = "/workspaces/TechStore/data/store.json"
clinet_path = "/workspaces/TechStore/data/client.json"

def get_products(data_path):
    with open(data_path, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_clinets(clinet_path):
    with open(clinet_path, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data
    
    
    
