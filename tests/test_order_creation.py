import allure


@allure.feature("Orders")
@allure.story("Create order")
class TestOrderCreation:
    @allure.title("Create order with authorization and ingredients")
    def test_create_order_authorized_with_ingredients_success(self, orders_api, created_user, ingredients_ids):
        response = orders_api.create_order(ingredients_ids, access_token=created_user["access_token"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "number" in body["order"]

    @allure.title("Create order without authorization and with ingredients")
    def test_create_order_unauthorized_with_ingredients_success(self, orders_api, ingredients_ids):
        response = orders_api.create_order(ingredients_ids)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "number" in body["order"]

    @allure.title("Create order without ingredients")
    def test_create_order_without_ingredients_returns_error(self, orders_api, created_user):
        response = orders_api.create_order([], access_token=created_user["access_token"])
        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Create order with wrong ingredients hash")
    def test_create_order_with_wrong_hash_returns_error(self, orders_api, created_user):
        response = orders_api.create_order(["invalid_hash"], access_token=created_user["access_token"])
        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert "message" in body
