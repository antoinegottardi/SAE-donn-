import requests
def requestsParking(x):
    response=requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml')
    return response.text

