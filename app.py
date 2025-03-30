import streamlit as st
import os

tasks_file = "tasks.txt"

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    st.title("📝 To-Do List App")
    st.subheader("Manage your tasks efficiently")

    tasks = load_tasks()
    
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            st.experimental_rerun()
        else:
            st.warning("Task cannot be empty!")

    if tasks:
        st.subheader("Your Tasks:")
        for i, task in enumerate(tasks):
            col1, col2 = st.columns([0.8, 0.2])
            col1.write(f"✅ {task}")
            if col2.button("Delete", key=i):
                tasks.pop(i)
                save_tasks(tasks)
                st.experimental_rerun()
    else:
        st.write("🎉 No tasks yet! Add some tasks above.")

if __name__ == "__main__":
    main()
