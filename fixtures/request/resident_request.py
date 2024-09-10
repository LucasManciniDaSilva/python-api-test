import random
import pytest
from utils.cpf_cnpj_generate import generate_cpf
from utils.file_reader import read_file
from faker import Faker
fake = Faker()


@pytest.fixture
def post_resident():
    apartment = random.randint(0, 10)
    email = fake.email()
    name = fake.name()

    payload = {
    "name": name,
    "email": email,
    "phone": "19999999999",
    "cpf": generate_cpf(),
    "block": "B",
    "apartment": f'{apartment}'
}

    yield payload
    
@pytest.fixture
def patch_resident():
    apartment = random.randint(0, 10)
    email = fake.email()
    name = fake.name()

    payload = {
    "name": name,
    "email": email,
    "phone": "19999999999",
    "cpf": generate_cpf(),
    "block": "B",
    "apartment": f'{apartment}'
}

    yield payload
    
@pytest.fixture
def post_resident_cpf_already_exists():
    apartment = random.randint(0, 10)
    email = fake.email()
    name = fake.name()

    payload = {
    "name": name,
    "email": email,
    "phone": "19999999999",
    "cpf": "47f68473777",
    "block": "B",
    "apartment": f'{apartment}'
}

    yield payload
    
@pytest.fixture
def post_resident_email_already_exists():
    apartment = random.randint(0, 10)
    name = fake.name()

    payload = {
    "name": name,
    "email": "joh9n@doae.coom",
    "phone": "19999999999",
    "cpf": generate_cpf(),
    "block": "B",
    "apartment": f'{apartment}'
}

    yield payload
    
@pytest.fixture
def post_resident_invalid_cpf():
    apartment = random.randint(0, 10)
    email = fake.email()
    name = fake.name()

    payload = {
    "name": name,
    "email": email,
    "phone": "19999999999",
    "cpf": "testes",
    "block": "B",
    "apartment": f'{apartment}'
}

    yield payload  