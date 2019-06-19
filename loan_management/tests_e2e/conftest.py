import pytest

from rest_framework_jwt.settings import api_settings
from loan_management.tests_e2e.factories import UserFactory


@pytest.fixture()
def token():
    user = UserFactory()

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)
