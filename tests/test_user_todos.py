import pytest
from utils.helpers import (
    get_users_in_fancode_city,
    get_user_todos,
    calculate_completion_percentage,
)
from utils.api_client import APIClient
from unittest.mock import patch

def test_fancode_users_exist():
    """Test that at least one user exists in FanCode city."""
    users = get_users_in_fancode_city()
    assert len(users) > 0, "No users found in FanCode city."

def test_fancode_user_todos_completion():
    """Test that FanCode users have more than 50% tasks completed."""
    users = get_users_in_fancode_city()
    for user in users:
        todos = get_user_todos(user["id"])
        completion_percentage = calculate_completion_percentage(todos)
        assert completion_percentage > 50, f"User {user['name']} failed with {completion_percentage:.2f}% completion."

def test_user_with_no_tasks():
    """Test user with no tasks."""
    with patch("utils.api_client.APIClient.get") as mock_get:
        mock_get.side_effect = lambda endpoint: [] if "todos" in endpoint else [{"id": 1, "name": "Test User"}]
        todos = get_user_todos(1)
        assert len(todos) == 0, "User should have no tasks."
        completion_percentage = calculate_completion_percentage(todos)
        assert completion_percentage == 0, "Completion percentage should be 0 for no tasks."

def test_user_with_all_incomplete_tasks():
    """Test user with all tasks incomplete."""
    todos = [{"userId": 1, "completed": False} for _ in range(10)]
    completion_percentage = calculate_completion_percentage(todos)
    assert completion_percentage == 0, "Completion percentage should be 0 for all incomplete tasks."

def test_api_failure():
    """Test API failure during user fetching."""
    with patch("utils.api_client.APIClient.get") as mock_get:
        mock_get.side_effect = Exception("API Failure")
        users = get_users_in_fancode_city()
        assert len(users) == 0, "No users should be returned on API failure."

if __name__ == "__main__":
    pytest.main()
