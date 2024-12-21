import streamlit as st
import pandas as pd

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame(
        columns=["ID", "Description", "Category", "Due Date", "Priority", "Status"]
    )

# Function to add a new task
def add_task(description, category, due_date, priority):
    if not description or not category or not priority:
        st.warning("Please fill in all the fields.")
        return
    if priority in st.session_state.tasks["Priority"].values:
        st.warning("Task with the same priority already exists!")
        return

    new_task = {
        "ID": len(st.session_state.tasks) + 1,
        "Description": description,
        "Category": category,
        "Due Date": due_date,
        "Priority": priority,
        "Status": "Pending"
    }
    st.session_state.tasks = pd.concat([st.session_state.tasks, pd.DataFrame([new_task])], ignore_index=True)
    st.success("Task added successfully!")

# Function to delete a task
def delete_task(task_id):
    if task_id not in st.session_state.tasks["ID"].values:
        st.warning("Task ID not found.")
        return
    
    task_status = st.session_state.tasks.loc[st.session_state.tasks["ID"] == task_id, "Status"].values[0]
    if task_status != "Completed":
        st.warning("Only completed tasks can be deleted.")
        return

    st.session_state.tasks = st.session_state.tasks[st.session_state.tasks["ID"] != task_id].reset_index(drop=True)
    st.success("Task deleted successfully!")

# Function to mark a task as completed
def mark_task_completed(task_id):
    if task_id not in st.session_state.tasks["ID"].values:
        st.warning("Task ID not found.")
        return

    st.session_state.tasks.loc[st.session_state.tasks["ID"] == task_id, "Status"] = "Completed"
    st.success("Task marked as completed!")

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
        due_date = st.date_input("Due Date")
        priority = st.number_input("Priority", min_value=1, step=1)
        submitted = st.form_submit_button("Add Task")

        if submitted:
            add_task(description, category, due_date, priority)

# View Tasks Tab
with tabs[1]:
    st.subheader("Task List")
    if not st.session_state.tasks.empty:
        # Highlight statuses for better visualization
        def color_status(val):
            color = "green" if val == "Completed" else "red"
            return f"color: {color};"
        
        styled_df = st.session_state.tasks.style.applymap(color_status, subset=["Status"])
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.info("No tasks available.")

# Manage Tasks Tab
with tabs[2]:
    st.subheader("Manage Tasks")
    if not st.session_state.tasks.empty:
        with st.form("manage_form"):
            task_id_to_manage = st.number_input("Enter Task ID to Manage", min_value=1, step=1)

            col1, col2 = st.columns(2)
            with col1:
                mark_submitted = st.form_submit_button("Mark as Completed")
                if mark_submitted:
                    mark_task_completed(task_id_to_manage)

            with col2:
                delete_submitted = st.form_submit_button("Delete Task")
                if delete_submitted:
                    delete_task(task_id_to_manage)
    else:
        st.info("No tasks to manage.")
