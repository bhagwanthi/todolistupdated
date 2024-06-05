import streamlit as st
import datetime

# Function to load tasks for a specific date from a file
def load_tasks(date):
    try:
        with open(f"tasks_{date}.txt", "r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        tasks_with_descriptions = []
        for task in tasks:
            parts = task.split(":")
            task_text = parts[0]
            is_completed = parts[1] if len(parts) > 1 else "False"  # Ensure is_completed is present
            description = parts[2] if len(parts) > 2 else ""  # Ensure description is present
            tasks_with_descriptions.append((task_text, is_completed, description))
        return tasks_with_descriptions
    except FileNotFoundError:
        return []

# Function to save tasks for a specific date to a file
def save_tasks(date, tasks):
    with open(f"tasks_{date}.txt", "w") as file:
        for task in tasks:
            task_text, is_completed, description = task
            file.write(f"{task_text}:{is_completed}:{description}\n")

# Function to load completion status for all days
def load_completion_status():
    try:
        with open("completion_status.txt", "r") as file:
            completion_status = file.readlines()
        completion_status = {date: bool(status.strip()) for date, status in (line.split(":") for line in completion_status)}
    except FileNotFoundError:
        completion_status = {}
    return completion_status

# Function to save completion status for all days
def save_completion_status(completion_status):
    with open("completion_status.txt", "w") as file:
        for date, status in completion_status.items():
            file.write(f"{date}:{int(status)}\n")

# Function to display tasks for a specific date and mark them as completed
def display_tasks(date, tasks, completion_status):
    date_str = date.strftime("%Y-%m-%d")  # Convert date to string format
    all_completed = all(task[1] == "True" for task in tasks)
    for i, (task_text, is_completed, description) in enumerate(tasks):
        task_key = f"task_{date_str}_{i}"
        cols = st.columns([5, 1])
        task_text_input = cols[0].text_input(label="", key=task_key, value=task_text)
        completed = cols[1].checkbox(label="", key=f"checkbox_{date_str}_{i}", value=is_completed == "True")
        description = st.text_area(label="Description", key=f"description_{date_str}_{i}", value=description, height=50)

        tasks[i] = (task_text_input, str(completed), description)  # Update task with description
        if completed:
            st.markdown(f'<style>#{task_key} input {{margin-right:10px;}} #{task_key} input:checked + span {{background-color:green; border-color:green;}}</style>', unsafe_allow_html=True)
        else:
            st.markdown(f'<style>#{task_key} input {{margin-right:10px;}} #{task_key} input:checked + span {{background-color:red; border-color:red;}}</style>', unsafe_allow_html=True)

    # Show label if all tasks are completed
    if all_completed:
        st.markdown("### All tasks for the day are completed!")
        completion_status[date_str] = True  # Use string format for date
    else:
        completion_status[date_str] = False  # Use string format for date

    # Save tasks to file
    save_tasks(date, tasks)

    # Save completion status
    save_completion_status(completion_status)

# Main function
def main():
    # App title
    st.title("📅 To-Do List")

    # Date picker to select a specific day
    selected_date = st.date_input("Select a date", datetime.date.today())

    # Load existing tasks for the selected date
    tasks = load_tasks(selected_date)

    # Load completion status for all days
    completion_status = load_completion_status()

    # Add new task for the selected date
    new_task = st.text_input("➕ Enter a new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append((new_task, "False", ""))  # Initial description is empty
            save_tasks(selected_date, tasks)
            st.experimental_rerun()  # Rerun to immediately reflect the new task

    # Display tasks for the selected date
    st.subheader("📋 Your Tasks")
    if tasks:
        display_tasks(selected_date, tasks, completion_status)
    else:
        st.write("No tasks assigned.")

    # Button to indicate all tasks for the day are completed
    if tasks and all(task[1] == "True" for task in tasks):
        st.success("All tasks for the day are completed!")

# Run the main function
if __name__ == "__main__":
    main()
