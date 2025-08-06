import requests


class HunterAPIClient:
    BASE_URL = "https://api.hunter.io/v2"

    def __init__(self, api_key: str, timeout: int = 10):
        self.api_key = api_key
        self.timeout = timeout

    def _get(self, url: str, params: dict = {}) -> dict:
        params["api_key"] = self.api_key
        full_url = f"{self.BASE_URL}/{url}"
        try:
            response = requests.get(full_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except TimeoutError:
            return {"error": "Request timed out", "status_code": 408}
        except requests.exceptions.HTTPError as http_error:
            return {"error": f"HTTP error: {http_error}", "status_code": 400}

    def search_domain(self, domain: str, limit: int = 10, offset: int = 0) -> dict:
        return self._get("domain-search", {
            "domain": domain,
            "limit": limit,
            "offset": offset
        })

    def email_finder(self, domain: str, first_name: str, last_name: str, limit: int = 10, offset: int = 0) -> dict:
        return self._get("email-finder", {
            "domain": domain,
            "limit": limit,
            "offset": offset,
            "first_name": first_name,
            "last_name": last_name
        })

    def verify_email(self, email: str) -> dict:
        return self._get("email-verifier", {
            "email": email,
        })
