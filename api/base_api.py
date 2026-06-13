"""Base API client with common HTTP methods."""

from __future__ import annotations

import allure
import requests

from helpers.config import BASE_URL


class BaseApi:
    """Base API class with shared request logic."""

    def __init__(self, session: requests.Session | None = None, base_url: str = BASE_URL) -> None:
        self.session = session or requests.Session()
        self.base_url = base_url.rstrip("/")

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    @staticmethod
    def _headers(access_token: str | None = None) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if access_token:
            headers["Authorization"] = access_token
        return headers

    def request(
        self,
        method: str,
        path: str,
        access_token: str | None = None,
        **kwargs,
    ) -> requests.Response:
        with allure.step(f"{method.upper()} {path}"):
            headers = self._headers(access_token)
            custom_headers = kwargs.pop("headers", {})
            headers.update(custom_headers)
            response = self.session.request(
                method=method.upper(),
                url=self._url(path),
                headers=headers,
                **kwargs,
            )
            return response

    def get(self, path: str, access_token: str | None = None, **kwargs) -> requests.Response:
        return self.request("GET", path, access_token=access_token, **kwargs)

    def post(self, path: str, access_token: str | None = None, **kwargs) -> requests.Response:
        return self.request("POST", path, access_token=access_token, **kwargs)

    def put(self, path: str, access_token: str | None = None, **kwargs) -> requests.Response:
        return self.request("PUT", path, access_token=access_token, **kwargs)

    def patch(self, path: str, access_token: str | None = None, **kwargs) -> requests.Response:
        return self.request("PATCH", path, access_token=access_token, **kwargs)

    def delete(self, path: str, access_token: str | None = None, **kwargs) -> requests.Response:
        return self.request("DELETE", path, access_token=access_token, **kwargs)
