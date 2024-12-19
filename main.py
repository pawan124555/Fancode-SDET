from utils.helpers import get_users_in_fancode_city, get_user_todos, calculate_completion_percentage

def main():
    print("Fetching users in 'FanCode' city...")
    users = get_users_in_fancode_city()

    if not users:
        print("No users found in FanCode city!")
        return

    for user in users:
        user_id = user["id"]
        name = user["name"]
        print(f"\nProcessing user: {name} (ID: {user_id})")
        todos = get_user_todos(user_id)

        if not todos:
            print("  - No tasks found.")
            continue

        completion_percentage = calculate_completion_percentage(todos)
        print(f"  - Completion Percentage: {completion_percentage:.2f}%")
        if completion_percentage > 50:
            print("  - Status: ✅ Passed")
        else:
            print("  - Status: ❌ Failed")

if __name__ == "__main__":
    main()
