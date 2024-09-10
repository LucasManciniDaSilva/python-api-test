from assertpy.assertpy import assert_that
from utils.print_helpers import pretty_print
from schema import Schema

def validate_status_code_and_schema(response, statusCodeExpected, bodySchema):

    statusCode = response.status_code 
    
    responseBody = response.json()
    
    assert_that(statusCode).is_equal_to(statusCodeExpected)
    
    pretty_print(responseBody)
    
    Schema(bodySchema).validate(responseBody)
    
def validate_message_error(responseError, responseErrorExpected):
    
    responseBody = responseError.json()
    
    assert_that(responseBody).is_equal_to(responseErrorExpected)
    
    
    