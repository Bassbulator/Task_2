"""User API client."""

import allure

from api.base_api import BaseApi
from helpers.config import LOGIN_USER_PATH, REGISTER_USER_PATH, USER_PROFILE_PATH


class UserApi(BaseApi):
    """API client for user operations."""

    @allure.step("Create user")
    def create_user(self, payload: dict) -> object:
        return self.post(REGISTER_USER_PATH, json=payload)

    @allure.step("Login user")
    def login_user(self, email: str, password: str) -> object:
        return self.post(LOGIN_USER_PATH, json={"email": email, "password": password})

    @allure.step("Update user")
    def update_user(self, payload: dict, access_token: str | None = None) -> object:
        return self.patch(USER_PROFILE_PATH, access_token=access_token, json=payload)

    @allure.step("Delete user")
    def delete_user(self, access_token: str) -> object:
        return self.delete(USER_PROFILE_PATH, access_token=access_token)
