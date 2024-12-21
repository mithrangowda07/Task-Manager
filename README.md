# To-Do List Manager with Linked List

This project is a **To-Do List Manager** built using **Streamlit** and **Python**. It manages tasks using a **linked list** instead of a DataFrame, ensuring efficient task management without relying on external libraries for data storage. The application allows you to:

- Add new tasks with descriptions, categories, due dates, and priorities.
- View all tasks in a table.
- Mark tasks as completed.
- Delete completed tasks.

## Features

1. **Add Task**:
   - Users can input a task description, select a category, assign a priority, and set a due date.
   - Tasks with duplicate priorities are not allowed.

2. **View Tasks**:
   - All tasks are displayed in a table format with details such as ID, Description, Category, Due Date, Priority, and Status.
   - Task statuses are color-coded for better visualization.

3. **Manage Tasks**:
   - Users can mark tasks as completed.
   - Only completed tasks can be deleted.

## Technical Overview

### Linked List Implementation

This project uses a **custom linked list** implementation to manage tasks:

- `TaskNode`: Represents an individual task node containing the task's details and a reference to the next task.
- `TaskLinkedList`: Manages the linked list operations such as adding, deleting, and updating tasks.

### Task Operations

- **Add Task**:
  - Tasks are appended to the end of the linked list.
  - The priority field ensures uniqueness to prevent conflicts.

- **Delete Task**:
  - Tasks can only be deleted if their status is marked as "Completed."
  - The linked list is traversed to find and remove the specified task.

- **Mark Task as Completed**:
  - Tasks are marked as completed by updating their status in the linked list.

## Installation and Setup

Follow these steps to run the To-Do List Manager:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.7+ installed.
   - Install the required library:
     ```bash
     pip install streamlit
     ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the Application**:
   - Open your browser and navigate to the URL provided in the terminal (e.g., `http://localhost:8501`).

## Project Structure

```plaintext
├── app.py          # Main application file
├── README.md       # Project documentation
```

## Usage

1. Launch the application using the command `streamlit run app.py`.
2. Navigate between the three tabs:
   - **Add Task**: Input task details and click "Add Task" to save it.
   - **View Tasks**: View all tasks in a table.
   - **Manage Tasks**: Use the Task ID to mark tasks as completed or delete them.
3. Manage your tasks efficiently with the user-friendly interface!

## Future Enhancements

- Add functionality to sort tasks based on priority or due date.
- Save and load tasks from a file to persist data across sessions.
- Implement a search feature to filter tasks by category or description.