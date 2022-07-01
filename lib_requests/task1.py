import requests


def smart(url: str, *args: str) -> str:
    response = requests.get(url)
    iq = 0
    name = ''
    for i in response.json():
        if i['name'] in args and i['powerstats']['intelligence'] > iq:
            iq = i['powerstats']['intelligence']
            name = i['name']
    return name
print("Самый умный супергерой -")

if __name__ == '__main__':
    print(smart('https://akabab.github.io/superhero-api/api/all.json', 'Hulk', 'Thanos', 'Capitan America'))