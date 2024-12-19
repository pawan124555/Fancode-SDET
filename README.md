Below is the complete **README.md** file for your project, including the setup process, file structure, and usage instructions.

---

# **FanCode SDET Assignment Solution**

This project is a solution to the FanCode SDET Assignment, which verifies that all users belonging to a specific city (`FanCode`) have more than 50% of their to-do tasks completed. The solution leverages the `jsonplaceholder` API to fetch data and validates the results.

---

## **Problem Statement**

### **Scenario**
- All users of the city **FanCode** must have more than half of their tasks (from `/todos` API) marked as completed.
- **FanCode** city is identified based on latitude (`lat`) between `-40` and `5` and longitude (`lng`) between `5` and `100` in the `/users` API.

---

## **Project Overview**

The project includes:
1. **API Client**: A reusable module to fetch data from APIs with error handling and retries.
2. **Helper Functions**: Logic to filter users, fetch tasks, and calculate task completion percentage.
3. **Test Cases**: Unit tests covering edge cases like missing tasks, incomplete tasks, and API failures.
4. **Main Script**: A standalone script to display results for users in the FanCode city.

---

## **File Structure**

```plaintext
project/
│
├── utils/                   # Utilities Folder
│   ├── __init__.py          # Makes 'utils' a package
│   ├── api_client.py        # API Client for fetching data
│   └── helpers.py           # Helper functions for processing data
│
├── tests/                   # Tests Folder
│   └── test_user_todos.py   # Test cases for validating scenarios
│
├── main.py                  # Main script to run the logic
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## **Setup and Installation**

### **Requirements**
Ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd <project-directory>
```

### **Step 2: Install Dependencies**
Install all required Python libraries using `requirements.txt`:
```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:
```
requests
pytest
```

---

## **How to Run**

### **Run the Main Script**
Execute the `main.py` file to fetch and display results for users in FanCode city:
```bash
python main.py
```

#### **Example Output**
```plaintext
Fetching users in 'FanCode' city...

Processing user: Leanne Graham (ID: 1)
  - Completion Percentage: 66.67%
  - Status: ✅ Passed

Processing user: Ervin Howell (ID: 2)
  - Completion Percentage: 40.00%
  - Status: ❌ Failed
```

---

### **Run the Test Cases**
Use `pytest` to run the unit tests located in the `tests` folder:
```bash
pytest tests/test_user_todos.py
```

#### **Sample Test Output**
```plaintext
================================================ test session starts ================================================
collected 5 items

tests/test_user_todos.py .....                                                                 [100%]

================================================ 5 passed in 0.12s =================================================
```

---

## **Code Details**

### **1. API Client**
- File: `utils/api_client.py`
- Handles API calls with retries and error handling.
```python
class APIClient:
    @staticmethod
    def get(endpoint, retries=3, timeout=5):
        # Fetch data with retries and timeout
```

### **2. Helper Functions**
- File: `utils/helpers.py`
- Functions:
  - `get_users_in_fancode_city()`: Fetch users belonging to FanCode city based on coordinates.
  - `get_user_todos(user_id)`: Fetch all tasks for a given user.
  - `calculate_completion_percentage(todos)`: Calculate the percentage of completed tasks.

### **3. Test Cases**
- File: `tests/test_user_todos.py`
- **Test Scenarios:**
  - Users in FanCode city exist.
  - Tasks completion percentage is greater than 50%.
  - User with no tasks.
  - User with all tasks incomplete.
  - Handling API failures gracefully.

---

## **Error Handling**

1. **API Errors**:
   - Retries up to 3 times in case of timeout, HTTP errors, or network issues.
2. **Data Validation**:
   - Handles missing or corrupt data.
   - Skips users with invalid latitude/longitude.
3. **Graceful Failures**:
   - Logs errors instead of crashing, ensuring smooth execution.

---

## **Edge Cases Covered**

- **No users found** in FanCode city.
- **User with no tasks** (empty `/todos` response).
- **User with all tasks incomplete**.
- **API failure**: Simulated errors using `unittest.mock`.

---

## **Future Improvements**

- Add integration tests for combining multiple APIs.
- Extend error handling for rate-limiting scenarios.
- Log API responses and execution details for better traceability.

---

## **Contact**

For questions or suggestions, please contact:

**Name**: [Your Name]  
**Email**: [Your Email]  

---

Enjoy coding! 🚀