"""Orders API client."""

import allure

from api.base_api import BaseApi
from helpers.config import INGREDIENTS_PATH, ORDERS_PATH


class OrdersApi(BaseApi):
    """API client for ingredients and orders."""

    @allure.step("Get ingredients")
    def get_ingredients(self) -> object:
        return self.get(INGREDIENTS_PATH)

    @allure.step("Create order")
    def create_order(self, ingredients: list[str], access_token: str | None = None) -> object:
        return self.post(ORDERS_PATH, access_token=access_token, json={"ingredients": ingredients})

    @allure.step("Get user orders")
    def get_user_orders(self, access_token: str | None = None) -> object:
        return self.get(ORDERS_PATH, access_token=access_token)
