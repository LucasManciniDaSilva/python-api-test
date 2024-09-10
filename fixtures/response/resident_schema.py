import uuid
import pytest


@pytest.fixture
def resident_schema():
    residentSchema = {
        "id": str,
        "createdAt": str,
        "updatedAt": str,
        "name": str,
        "email": str,
        "phone": str,
        "cpf": str,
        "block": str,
        "apartment": str
}
    
    yield residentSchema
    
@pytest.fixture
def get_all_resident_schema():
    getAllSchema = [{
        "id": str,
        "createdAt": str,
        "updatedAt": str,
        "name": str,
        "email": str,
        "phone": str,
        "cpf": str,
        "block": str,
        "apartment": str
}]
    

    yield getAllSchema
    
@pytest.fixture
def resident_error_schema():
    residentError = {
    "name": str,
    "message": str
}
    

    yield residentError
