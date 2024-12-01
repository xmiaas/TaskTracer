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
    return print(tsk)


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


def tasker():
    print('Welcome to Task Tracker \nPrint /help to get a list of commands\nIf you want to exit write Exit')

    while True:
        message = input()
        if message == 'Exit' or message == 'exit':
            break
        if message[:3] == 'add':
            add_task(message[3:])
        if message == 'list':
            for i in get_tasks():
                print(f'{i["id"]}) {i["description"]}')
        if message[:6] == 'delete':
            delete_task(message[6:])
        if 'mark-in-progress' in message:
            mark_in_progres(message[16:])
        if 'mark-done' in message:
            mark_done(message[9:])


tasker()
