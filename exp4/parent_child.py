import os
def parent_child_id():
    prcs = os.fork()

    # prcs > 0 => parent process
    if prcs > 0:
        print("Parent process and id = ", os.getpid())

    # prcs = 0 => child process
    else:
        print("Child process and id = ", os.getpid())


parent_child_id()