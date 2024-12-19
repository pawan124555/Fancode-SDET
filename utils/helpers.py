from utils.api_client import APIClient

def get_users_in_fancode_city():
    """
    Fetch users belonging to the city 'FanCode' based on latitude and longitude.
    Returns:
        list: Users in 'FanCode' city
    """
    try:
        users = APIClient.get("users")
        fancode_users = []
        for user in users:
            try:
                lat = float(user['address']['geo']['lat'])
                lng = float(user['address']['geo']['lng'])
                if -40 <= lat <= 5 and 5 <= lng <= 100:
                    fancode_users.append(user)
            except (KeyError, ValueError):
                print(f"Skipping user due to invalid coordinates: {user}")
        return fancode_users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

def get_user_todos(user_id):
    """
    Fetch all todos for a given user.
    Args:
        user_id (int): User ID
    Returns:
        list: Todos for the user
    """
    try:
        todos = APIClient.get("todos")
        return [todo for todo in todos if todo.get("userId") == user_id]
    except Exception as e:
        print(f"Error fetching todos for user {user_id}: {e}")
        return []

def calculate_completion_percentage(todos):
    """
    Calculate the completion percentage of a user's todos.
    Args:
        todos (list): List of todos
    Returns:
        float: Percentage of completed tasks
    """
    try:
        completed = len([todo for todo in todos if todo.get("completed")])
        total = len(todos)
        return (completed / total * 100) if total > 0 else 0
    except Exception as e:
        print(f"Error calculating completion percentage: {e}")
        return 0.0
