import requests
from json import dumps
from config import BASE_URI

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def getHealth():
    response = requests.get(f'{BASE_URI}/health')
    return response


def postResident(payload):
    response = requests.post(url=f'{BASE_URI}/residents', data=payload, headers=headers)
    return response

def getAllResidents():
    response = requests.get(f'{BASE_URI}/residents')
    return response

def getResident(residentId):
    response = requests.get(f'{BASE_URI}/residents/{residentId}')
    return response


def patchResident(payload, residentId):
    response = requests.patch(url=f'{BASE_URI}/residents/{residentId}', data=payload, headers=headers)
    return response
