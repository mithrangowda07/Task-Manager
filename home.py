import streamlit as st
from datetime import date
import pandas as pd

# Node class for the linked list
class TaskNode:
    def __init__(self, task_id, description, category, due_date, priority, status="Pending"):
        self.task_id = task_id
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.next = None

# Linked list class to manage tasks
class TaskLinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, description, category, due_date, priority):
        # Check if a task with the same priority already exists
        current = self.head
        while current:
            if current.priority == priority:
                st.warning("Task with the same priority already exists!")
                return False
            current = current.next

        # Add the new task to the list
        new_task_id = self.get_next_id()
        new_task = TaskNode(new_task_id, description, category, due_date, priority)
        if not self.head:
            self.head = new_task
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_task
        st.success("Task added successfully!")
        return True

    def delete_task(self, task_id):
        if not self.head:
            st.warning("Task list is empty.")
            return False

        # If the head is the task to delete
        if self.head.task_id == task_id:
            if self.head.status != "Completed":
                st.warning("Only completed tasks can be deleted.")
                return False
            self.head = self.head.next
            st.success("Task deleted successfully!")
            return True

        # Search for the task in the list
        current = self.head
        while current.next and current.next.task_id != task_id:
            current = current.next

        if current.next and current.next.status == "Completed":
            current.next = current.next.next
            st.success("Task deleted successfully!")
            return True
        else:
            st.warning("Task ID not found or not completed.")
            return False

    def mark_task_completed(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                current.status = "Completed"
                st.success("Task marked as completed!")
                return True
            current = current.next
        st.warning("Task ID not found.")
        return False

    def get_next_id(self):
        if not self.head:
            return 1
        current = self.head
        max_id = 1
        while current:
            if current.task_id > max_id:
                max_id = current.task_id
            current = current.next
        return max_id + 1

    def to_list(self):
        tasks = []
        current = self.head
        while current:
            tasks.append({
                "ID": current.task_id,
                "Description": current.description,
                "Category": current.category,
                "Due Date": current.due_date,
                "Priority": current.priority,
                "Status": current.status,
            })
            current = current.next
        return sorted(tasks, key=lambda x: x["Priority"])


# Initialize the task linked list
if "task_list" not in st.session_state:
    st.session_state.task_list = TaskLinkedList()

# Streamlit UI design
st.title("📝 To-Do List Manager")
st.markdown(
    """
    **Welcome to your task manager!**
    - Add, view, and manage your tasks.
    - Ensure every task is completed before deleting.
    """
)

# Tabs for better organization
tabs = st.tabs(["📋 Add Task", "📊 View Tasks", "⚙️ Manage Tasks"])

# Add Task Tab
with tabs[0]:
    st.subheader("Add a New Task")
    with st.form("task_form", clear_on_submit=True):
        description = st.text_input("Task Description", placeholder="Enter task description")
        category = st.selectbox("Category", ["Work", "Personal", "Shopping", "Fitness"], index=0)
        due_date = st.date_input("Due Date", value=date.today())
        priority = st.number_input("Priority", min_value=1, step=1)
        submitted = st.form_submit_button("Add Task")

        if submitted:
            st.session_state.task_list.add_task(description, category, due_date, priority)

# View Tasks Tab
with tabs[1]:
    st.subheader("Task List")
    tasks = st.session_state.task_list.to_list()
    if tasks:
        st.write(pd.DataFrame(tasks))
    else:
        st.info("No tasks available.")

# Manage Tasks Tab
with tabs[2]:
    st.subheader("Manage Tasks")
    if st.session_state.task_list.head:
        with st.form("manage_form"):
            task_id_to_manage = st.number_input("Enter Task ID to Manage", min_value=1, step=1)

            col1, col2 = st.columns(2)
            with col1:
                mark_submitted = st.form_submit_button("Mark as Completed")
                if mark_submitted:
                    st.session_state.task_list.mark_task_completed(task_id_to_manage)

            with col2:
                delete_submitted = st.form_submit_button("Delete Task")
                if delete_submitted:
                    st.session_state.task_list.delete_task(task_id_to_manage)
    else:
        st.info("No tasks to manage.")
