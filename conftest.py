import allure
import pytest

from api.orders_api import OrdersApi
from api.user_api import UserApi
from helpers.data_generator import generate_user_payload


@pytest.fixture
def user_api() -> UserApi:
    return UserApi()


@pytest.fixture
def orders_api() -> OrdersApi:
    return OrdersApi()


@pytest.fixture
def created_user(user_api: UserApi) -> dict[str, str]:
    payload = generate_user_payload()

    with allure.step("Create user for test setup"):
        response = user_api.create_user(payload)
        body = response.json()

    access_token = body["accessToken"]
    data = {"access_token": access_token, **payload}

    yield data

    with allure.step("Delete user during teardown"):
        user_api.delete_user(access_token)


@pytest.fixture
def ingredients_ids(orders_api: OrdersApi) -> list[str]:
    with allure.step("Load ingredient ids for order tests"):
        response = orders_api.get_ingredients()
        body = response.json()
    return [body["data"][0]["_id"], body["data"][1]["_id"]]
