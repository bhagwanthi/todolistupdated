import streamlit as st
import datetime

# Function to load tasks for a specific date from a file
def load_tasks(date):
    try:
        with open(f"tasks_{date}.txt", "r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks for a specific date to a file
def save_tasks(date, tasks):
    with open(f"tasks_{date}.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load completed tasks for a specific date from a file
def load_completed_tasks(date):
    try:
        with open(f"completed_tasks_{date}.txt", "r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save completed tasks for a specific date to a file
def save_completed_tasks(date, tasks):
    with open(f"completed_tasks_{date}.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks for a specific date
def display_tasks(date, tasks, completed_tasks):
    for i, task in enumerate(tasks):
        task_key = f"task_{date}_{i}"
        task_text = st.text_input(label="", key=task_key, value=task)
        is_completed = st.checkbox(label="", key=f"checkbox_{date}_{i}")
        if is_completed:
            completed_tasks.append(task_text)
            tasks.pop(i)
            save_tasks(date, tasks)
            save_completed_tasks(date, completed_tasks)
            st.experimental_rerun()

# Main function
def main():
    # App title
    st.title("📅 To-Do List")

    # Date picker to select a specific day
    selected_date = st.date_input("Select a date", datetime.date.today())

    # Load existing tasks and completed tasks for the selected date
    tasks = load_tasks(selected_date)
    completed_tasks = load_completed_tasks(selected_date)

    # Add new task for the selected date
    new_task = st.text_input("➕ Enter a new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append(new_task)
            save_tasks(selected_date, tasks)
            st.experimental_rerun()

    # Display pending tasks and completed tasks in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Your Tasks")
        if tasks:
            display_tasks(selected_date, tasks, completed_tasks)
        else:
            st.write("No tasks available.")

    with col2:
        st.subheader("✅ Completed Tasks")
        if completed_tasks:
            for task in completed_tasks:
                st.write(task)
        else:
            st.write("No completed tasks.")

# Run the main function
if __name__ == "__main__":
    main()
