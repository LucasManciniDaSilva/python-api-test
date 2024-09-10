from json import dumps
import requests
from routes.residents_api import patchResident
from utils.assertion import *
from fixtures.response.resident_response import *
from db.connection import select_resident_id
from fixtures.response.resident_schema import *
from fixtures.request.resident_request import *
       


def test_update_resident(patch_resident, resident_schema):
    '''Resident Suite - Atualizar um Residente'''
    
    userId = select_resident_id()

    residentResponse = patchResident(dumps(patch_resident), userId)

    validate_status_code_and_schema(residentResponse, requests.codes.ok, resident_schema)
    

def test_patch_resident_invalid_id(patch_resident, invalid_resident_id, resident_error_schema):
    '''Resident Suite - Atualizar um Residente informando um id inválido - Error'''

    residentResponse = patchResident(dumps(patch_resident), "testes")
    
    validate_message_error(residentResponse, invalid_resident_id)

    validate_status_code_and_schema(residentResponse, requests.codes.bad_request, resident_error_schema)
    
    
def test_patch_resident_nonexistent_id(patch_resident, nonexistent_resident_id, resident_error_schema):
    '''Resident Suite - Atualizar um Residente informando um id não existente - Error'''
    
    residentResponse = patchResident(dumps(patch_resident), "24d8ae85-2415-4e62-b25f-e789bbeb1f4c")
    
    validate_message_error(residentResponse, nonexistent_resident_id)

    validate_status_code_and_schema(residentResponse, requests.codes.not_found, resident_error_schema)