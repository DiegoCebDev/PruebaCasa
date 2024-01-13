import requests

def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(type(r.text))
    categories=r.json()
    for m in categories:
        print("Iterando lista json",m['name'])