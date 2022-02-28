import json
import arrow

todos = []

def add_todo():
    task = 0
    if len(todos) > 0:
        task = todos[-1]["task"] + 1
    date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
    text = input("Enter content: ")
    complete = False
    new_todo = {
        "task": task,
        "created_at": arrow.get(date).replace(tzinfo='Asia/Ha_Noi').isoformat(),
        "text": text,
        "complete": complete
    }
    todos.append(new_todo)
    with open("todos.json", "w") as jsonfile:
        json.dump(todos, jsonfile, default=lambda dt: dt.isoformat(), indent=2)

def show_todos():
    print("{:<20} {:<20} {:<25} {:<20}".format('Task', 'Created at', 'Content', 'Status'))
    print("{:<20} {:<20} {:<25} {:<20}".format('-----------', '---------------', '-------------------', '----------'))
    pending = 0
    complete = 0
    for todo in todos:
        format_todo = {**todo}
        format_todo["created_at"] = arrow.get(todo["created_at"]).humanize(locale="vi")
        if todo["complete"] == True:
            complete += 1
            format_todo["complete"] = "Completed"
        else:
            pending += 1
            format_todo["complete"] = "Pending"
        print("{:<5}{:<15} {:<20} {:<25} {:<20}".format('', format_todo["task"], format_todo["created_at"], format_todo["text"], format_todo["complete"]))
    print(f"\nPending: {pending}, Completed: {complete}")
    print("{:<20} {:<20} {:<25} {:<20}".format('------------------', '-----------------', '--------------------', '-----------------'))
    
def choose_todos():
    act = input("> [N] New Todo ~ [C] Complete ~ [H] Show list content ~ (Q) Quit: ")    
    act.lower()
    if act == "n":
        add_todo()
        show_todos()
        choose_todos()
    if act == "c":
        show_todos()
        i = int(input("Nhập mã công việc đã hoàn thành: "))
        task = todos[i]
        task["complete"] = True
        with open("todos.json", "w") as jsonfile:
            json.dump(todos, jsonfile, default=lambda dt: dt.isoformat(), indent=2, ensure_ascii=False)
        choose_todos()
    if act == "h":
        show_todos()
        choose_todos()
    if act == "q":
        print()
    else:
        print('Cú pháp không chinh xác, vui lòng nhập lại.')
        choose_todos()