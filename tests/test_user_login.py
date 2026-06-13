import allure

@allure.feature("User")
@allure.story("Login")
class TestUserLogin:
    @allure.title("Login with existing user")
    def test_login_existing_user_success(self, user_api, created_user):
        response = user_api.login_user(created_user["email"], created_user["password"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Login with wrong credentials")
    def test_login_with_wrong_credentials_returns_error(self, user_api, created_user):
        response = user_api.login_user("wrong_login@ya.ru", "wrong_password")
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"
