import requests
from fixtures.response.resident_response import invalid_resident_id, nonexistent_resident_id
from routes.residents_api import getResident
from utils.assertion import *
from db.connection import select_resident_id
from fixtures.response.resident_schema import *
from fixtures.request.resident_request import *
    
def test_get_resident(resident_schema):
    '''Resident Suite - Busca de um Residente'''
     
    userId = select_resident_id()

    residentResponse = getResident(userId)

    validate_status_code_and_schema(residentResponse, requests.codes.ok, resident_schema)
    
def test_get_resident_invalid_id(invalid_resident_id, resident_error_schema):
    '''Resident Suite - Busca de um Residente informando um id inválido - Error'''

    residentResponse = getResident("testes")
    
    validate_message_error(residentResponse, invalid_resident_id)

    validate_status_code_and_schema(residentResponse, requests.codes.bad_request, resident_error_schema)
    
def test_get_resident_nonexistent_id(nonexistent_resident_id, resident_error_schema):
    '''Resident Suite - Busca de um Residente informando um id não existente - Error'''

    residentResponse = getResident("24d8ae85-2415-4e62-b25f-e789bbeb1f4c")
    
    validate_message_error(residentResponse, nonexistent_resident_id)

    validate_status_code_and_schema(residentResponse, requests.codes.not_found, resident_error_schema)
    


