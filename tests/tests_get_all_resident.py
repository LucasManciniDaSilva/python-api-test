import requests
from routes.residents_api import getAllResidents
from utils.assertion import *
from fixtures.response.resident_schema import *
from fixtures.request.resident_request import *
       

def test_get_all_residents(get_all_resident_schema):
    '''Resident Suite - Busca de todos os Residentes'''

    residentResponse = getAllResidents()

    validate_status_code_and_schema(residentResponse, requests.codes.ok, get_all_resident_schema)
    
