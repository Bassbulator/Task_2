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
def new_user_payload() -> dict[str, str]:
    return generate_user_payload()


@pytest.fixture
def created_user(user_api: UserApi, new_user_payload: dict[str, str]) -> dict[str, str]:
    with allure.step("Create user for test setup"):
        response = user_api.create_user(new_user_payload)
        body = response.json()

    access_token = body["accessToken"]
    data = {"access_token": access_token, **new_user_payload}

    yield data

    with allure.step("Delete user during teardown"):
        user_api.delete_user(access_token)


@pytest.fixture
def registered_user(user_api: UserApi, new_user_payload: dict[str, str]) -> dict[str, str]:
    with allure.step("Register user for test setup"):
        response = user_api.create_user(new_user_payload)
        body = response.json()

    data = {"response": response, "body": body, **new_user_payload, "access_token": body["accessToken"]}

    yield data

    with allure.step("Delete registered user during teardown"):
        user_api.delete_user(data["access_token"])


@pytest.fixture
def ingredients_ids(orders_api: OrdersApi) -> list[str]:
    with allure.step("Load ingredient ids for order tests"):
        response = orders_api.get_ingredients()
        body = response.json()
    return [body["data"][0]["_id"], body["data"][1]["_id"]]
