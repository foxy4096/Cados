from django.conf import settings
from ninja.security import APIKeyHeader


class ApiKey(APIKeyHeader):
    """
    Authenticate the User
    """

    param_name: str = "X-API-Key"

    def authenticate(self, request, key: str):
        """
        Check if the `X-API-Key` in the header is equal to\\
        `API_AUTH_KEY` variable in the `settings.py`
        """
        if key == settings.API_AUTH_KEY:
            return key
