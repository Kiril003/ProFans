def add_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                task, status = line.strip().split('|')
                tasks.append({"task": task, "done": status == "True"})
    except FileNotFoundError:
        pass
    return tasks

def edit_tasks():
    pass

def delete_tasks():
    pass

def completed_tasks():
    pass

def main():
    pass