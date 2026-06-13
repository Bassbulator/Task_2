import allure

from helpers.data_generator import generate_user_payload


@allure.feature("User")
@allure.story("Create user")
class TestUserRegistration:
    @allure.title("Create unique user")
    def test_create_unique_user_success(self, user_api):
        payload = generate_user_payload()

        with allure.step("Register new user"):
            response = user_api.create_user(payload)
        body = response.json()

        try:
            assert response.status_code == 200
            assert body["success"] is True
            assert "accessToken" in body
            assert "refreshToken" in body
        finally:
            if body.get("accessToken"):
                user_api.delete_user(body["accessToken"])

    @allure.title("Create already registered user")
    def test_create_existing_user_returns_error(self, user_api, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"],
            "name": created_user["name"],
        }
        response = user_api.create_user(payload)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "User already exists"

    @allure.title("Create user without required field")
    def test_create_user_without_email_returns_error(self, user_api):
        payload = generate_user_payload()
        payload_without_email = {"password": payload["password"], "name": payload["name"]}

        response = user_api.create_user(payload_without_email)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"
