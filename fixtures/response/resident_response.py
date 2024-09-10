import pytest


@pytest.fixture
def empty_request_body():
    payload = {
    "name": "InvalidFieldsError",
    "message": "Missing fields: name, email, phone, cpf, block, apartment"
}

    yield payload
    
@pytest.fixture
def user_already_exists():
    payload = {
    "name": "AlreadyExistsException",
    "message": "Resident already exists"
}

    yield payload
    
@pytest.fixture
def invalid_cpf():
    payload = {
    "name": "InvalidFieldsError",
    "message": "Invalid CPF provided"
}

    yield payload
    
@pytest.fixture
def invalid_resident_id():
    payload = {
    "name": "BadRequestException",
    "message": "Invalid id"
}
    yield payload
    
@pytest.fixture
def nonexistent_resident_id():
    payload = {
    "name": "NotFoundException",
    "message": "Resident not found"
}

    yield payload