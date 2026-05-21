import allure


@allure.feature("Orders")
@allure.story("Get user orders")
class TestGetUserOrders:
    @allure.title("Get orders for authorized user")
    def test_get_orders_authorized_user_success(self, orders_api, created_user, ingredients_ids):
        orders_api.create_order(ingredients_ids, access_token=created_user["access_token"])

        response = orders_api.get_user_orders(access_token=created_user["access_token"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "orders" in body

    @allure.title("Get orders without authorization")
    def test_get_orders_unauthorized_returns_error(self, orders_api):
        response = orders_api.get_user_orders()
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"
