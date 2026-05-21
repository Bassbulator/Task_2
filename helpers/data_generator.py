"""Test data generators."""

from uuid import uuid4


def generate_user_payload() -> dict[str, str]:
    """Return unique user payload."""
    suffix = uuid4().hex[:10]
    return {
        "email": f"autotest_{suffix}@ya.ru",
        "password": f"Pass_{suffix}",
        "name": f"User_{suffix}",
    }
