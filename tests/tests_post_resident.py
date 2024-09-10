from json import dumps
import requests
from routes.residents_api import postResident
from utils.assertion import *
from fixtures.response.resident_response import *
from fixtures.response.resident_schema import *
from fixtures.request.resident_request import *



def test_create_resident(post_resident, resident_schema):
    '''Resident Suite - Criação de um Residente com Sucesso'''

    residentResponse = postResident(dumps(post_resident))

    validate_status_code_and_schema(residentResponse, requests.codes.created, resident_schema)


def test_empty_body(resident_error_schema, empty_request_body):
    '''Resident Suite - Informando um requestBody vazio - Erro'''

    residentResponse = postResident(dumps({}))

    validate_message_error(residentResponse, empty_request_body)

    validate_status_code_and_schema(residentResponse, requests.codes.bad_request, resident_error_schema)
    

def test_cpf_already_exists(post_resident_cpf_already_exists, user_already_exists, resident_error_schema):
    '''Resident Suite - Informando um cpf já existente- Erro'''

    residentResponse = postResident(dumps(post_resident_cpf_already_exists))

    validate_message_error(residentResponse, user_already_exists)

    validate_status_code_and_schema(residentResponse, requests.codes.conflict, resident_error_schema)
    

def test_email_already_exists(post_resident_email_already_exists, user_already_exists, resident_error_schema):
    '''Resident Suite - Informando um email já existente- Erro'''

    residentResponse = postResident(dumps(post_resident_email_already_exists))

    validate_message_error(residentResponse, user_already_exists)

    validate_status_code_and_schema(residentResponse, requests.codes.conflict, resident_error_schema)
    

def test_invalid_cpf(post_resident_invalid_cpf, invalid_cpf, resident_error_schema):
    '''Resident Suite - Informando um cpf inválido- Erro'''

    residentResponse = postResident(dumps(post_resident_invalid_cpf))

    validate_message_error(residentResponse, invalid_cpf)

    validate_status_code_and_schema(residentResponse, requests.codes.bad_request, resident_error_schema)