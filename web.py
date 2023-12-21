import streamlit as st
import functions

#todos list
todos = functions.get_todos()

#callback add function
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#create streamlit elements
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

#complete function
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        #delete in todos.txt
        functions.write_todos(todos)
        #delete in streamlit dictionary
        del st.session_state[todo]
        st.experimental_rerun()

#input to add item
st.text_input(label="Add new todo",
              #placeholder="Add new todo..",
              on_change= add_todo,
              key="new_todo")

#for checking only
#st.session_state