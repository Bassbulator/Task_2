import allure

@allure.feature("User")
@allure.story("Create user")
class TestUserRegistration:
    @allure.title("Create unique user")
    def test_create_unique_user_success(self, registered_user):
        response = registered_user["response"]
        body = registered_user["body"]

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body

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
    def test_create_user_without_email_returns_error(self, user_api, new_user_payload):
        payload = {"password": new_user_payload["password"], "name": new_user_payload["name"]}
        response = user_api.create_user(payload)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"
