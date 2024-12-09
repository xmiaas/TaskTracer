import json
import datetime


def write_to_file(where):
    with open('tasks.json', 'w') as f:
        for i in where:
            json.dump(i, f)
            f.write('\n')


# add task
def add_task(desc):
    list_num = []

    data = {'id': 'None',
            'description': desc,
            'status': 'todo',
            'createDAT': f'{datetime.datetime.now()}',
            'updatedAt': None}

    if len(get_tasks()) != 0:
        for i in get_tasks():
            list_num.append(i['id'])
        list_num.sort()
        num = int(list_num[-1]) + 1
    else:
        num = 1
    data['id'] = num
    with open('tasks.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')


def update_task(ind, inp):
    tasks = get_tasks()
    for i in tasks:
        if int(i['id']) == int(ind):
            i['description'] = ' '.join(inp)
            i['updatedAt'] = f'{datetime.datetime.now()}'
    write_to_file(tasks)


# get all task
def get_tasks():
    with open('tasks.json', 'r') as file:
        tasks = []
        for i in file:
            tasks.append(json.loads(i))

    return tasks


# delete one task
def delete_task(num):
    tsk = get_tasks()
    for i in tsk:
        if int(i['id']) == int(num):
            ind = tsk.index(i)
            del tsk[ind]
            break
    for i in range(len(tsk)):
        tsk[i]['id'] = i + 1

    write_to_file(tsk)


def mark_in_progres(ind):
    tsk = get_tasks()
    for i in tsk:
        if int(i['id']) == int(ind):
            i['status'] = 'in-progress'
    write_to_file(tsk)


def mark_done(ind):
    tsk = get_tasks()
    for i in tsk:
        if int(i['id']) == int(ind):
            i['status'] = 'done'
    write_to_file(tsk)


def lists(inp):
    for i in get_tasks():
        if i['status'] == inp:
            print(f'{i["id"]}){i["description"]}')


def tasker():
    print('Welcome to Task Tracker \nPrint /help to get a list of commands\nIf you want to exit write Exit')

    while True:
        message = input()
        if message == 'Exit' or message == 'exit':
            break
        if message == '/help':
            print("""Write 'list' to see the list of all tasks.
Write 'add' and name of task separated by space to add task.
Write 'update' and the index of the task from the list to update it.
Write 'delete' and the index of the task from the list to delete it.
Write 'mark-in-progress' and the index of the task from the list to change status of task to "in-progress".
Write 'mark-done' and the index of the task from the list to change status of task to "in-progress".
Write 'list done' or 'list todo' or 'list in-progress' to view a tasks by status".

            """)
        if message[:3] == 'add':
            add_task(message[3:])
            print('Task added')
        if 'list' in message:
            x = message.split()
            if len(x) == 1:
                for i in get_tasks():
                    tx = f'{i["id"]}){i["description"]}.'
                    print(tx.replace(' ', ''), 'Status:', i['status'])

            else:
                lists(x[-1])

        if message[:6] == 'delete':
            delete_task(message[6:])
            print('Task deleted')
        if 'mark-in-progress' in message:
            mark_in_progres(message[16:])
        if 'mark-done' in message:
            mark_done(message[9:])
        if 'update' in message:
            wrt = message.split()
            update_task(ind=wrt[1], inp=wrt[2:])
            print('Task updated')


tasker()
