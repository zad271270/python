

todos = []


while True:
    user_action = input("Type 1 for add or 2 for show or 3 for exit or 4 for edit or 5 for remove: ")
    user_action = user_action.strip()

    match user_action:
        case "1" | "add":
            todo = input("enter a todo :")
            todos.append(todo)
        case "2" | "show":

            for index, item in enumerate(todos):
                item = item.title()
                row = f'{index}----{item}'
                print(row)

        case "3" | "exit":
            break
        case "4" | "edit":
            number = int(input("Enter de Number of the todo list to edit"))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo

        case "5" | "remove":
            number = int(input("number of the todo list to remove"))
            todos.pop(number)

        case whatever:
            print("what da fuck?????")


print("Bye!!!!!!!")
