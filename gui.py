import functions
import PySimpleGUI as sg
import time
import os

#create todos.txt if not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

#theme
sg.theme('DarkTeal4')

# Create GUI elements
clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter a todo', key='todo')
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                         key='todos',
                         enable_events=True,
                         size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Create the main window
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',15))

# Main event loop
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value= time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    # Handle events using a match statement
    match event:
        case 'Add' :
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case 'Complete':
            try :
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case 'Exit':
            break

        case'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            # Exit the loop when the window is closed
            break

# Close the window when the loop ends
window.close()