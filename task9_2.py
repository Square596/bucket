import os


class DisconnectUser(Exception):
    pass


def write_to_file(f_obj):
    while True:
        try:
            message = yield
            f_obj.write(message+'\n')
        except DisconnectUser:
            break


def connect_user():
    home_path = os.path.expanduser("~")
    working_dir = os.path.join(home_path, 'hw9')
    os.makedirs(working_dir, exist_ok=True)
    while True:
        user_id = yield
        file = open(os.path.join(working_dir, user_id+'.txt'), 'a+')
        yield from write_to_file(file)
        file.close()


def scheduler(path):
    connected = dict() #users who are connected right now
    with open(path, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break

            line = line.rstrip('\n').split(' ')

            if line[0] == 'auth':
                connected[line[1]] = connect_user()
                next(connected[line[1]])
                connected[line[1]].send(line[1])

            elif line[0] == 'disconnect':
                if line[1] in connected:
                    connected[line[1]].throw(DisconnectUser)
                    connected[line[1]].close()
                    connected.pop(line[1], None)

            elif line[0] in connected:
                    connected[line[0]].send(line[1])


if __name__ == '__main__':
    path = input() #the data file is also posted on github
    scheduler(path)