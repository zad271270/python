

while True:
    user_action = input("/-1 for add/-2 for show/-3 for remove/-4 for edit/-5 for exit: ")
    user_action = user_action.strip()
    match user_action:
        case "1" | "add":
            todo = input("enter a todo :") + "\n"

            file = open('files/todos.txt', 'r')
            todos =file.readlines()
            file.close()


            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()


        case "2" | "show":

            file = open('files/todos.txt', 'r')
            todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.title()
                row = f'{index}----{item}'
                print(row)
            file.close()

        case "3" | "remove":
            file = open('files/todos.txt', 'r')
            todos = file.readlines()

            number = int(input("number of the todo list to remove: "))
            todos.pop(number)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "4" | "edit":
            number = int(input("Enter de Number of the todo list to edit:  "))


            file = open('files/todos.txt', 'r')
            todos = file.readlines()

            new_todo = input("Enter the edit todo: ")
            todos[number] = new_todo

            file = open('files/todos.txt', 'w')
            file.writelines(todos[number])
            file.close()


        case "5" | "exit":
            break
        case whatever:
            print("what da fuck?????")
print("Bye!!!!!!!")
