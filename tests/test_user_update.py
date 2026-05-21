import allure


@allure.feature("User")
@allure.story("Update profile")
class TestUserUpdate:
    @allure.title("Update email with authorization")
    def test_update_email_authorized_success(self, user_api, created_user):
        new_email = f"updated_{created_user['email']}"

        response = user_api.update_user(
            {"email": new_email},
            access_token=created_user["access_token"],
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == new_email

    @allure.title("Update name with authorization")
    def test_update_name_authorized_success(self, user_api, created_user):
        new_name = f"{created_user['name']}_updated"

        response = user_api.update_user(
            {"name": new_name},
            access_token=created_user["access_token"],
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["name"] == new_name

    @allure.title("Update password with authorization")
    def test_update_password_authorized_success(self, user_api, created_user):
        new_password = f"{created_user['password']}_updated"

        response = user_api.update_user(
            {"password": new_password},
            access_token=created_user["access_token"],
        )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Update email without authorization")
    def test_update_email_unauthorized_returns_error(self, user_api, created_user):
        response = user_api.update_user({"email": f"new_{created_user['email']}"})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Update name without authorization")
    def test_update_name_unauthorized_returns_error(self, user_api, created_user):
        response = user_api.update_user({"name": f"{created_user['name']}_new"})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Update password without authorization")
    def test_update_password_unauthorized_returns_error(self, user_api, created_user):
        response = user_api.update_user({"password": f"{created_user['password']}_new"})
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"
