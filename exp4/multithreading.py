import os
import threading
import math


def print_factorial(num):
    print("Factorial operation assigned to thread: {}".format(threading.current_thread().name))
    # print("ID of process running Factorial Thread: {}".format(os.getpid()))
    """
    function to print cube of given num
    """
    print("Factorial: {}".format(math.factorial(num)))
  
def print_square(num):
    print("Square operation assigned to thread: {}".format(threading.current_thread().name))
    # print("ID of process running Square Thread: {}".format(os.getpid()))
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    num = int(input("Enter Number : "))
    # print("ID of process running main program: {}".format(os.getpid()))
    # creating thread
    t1 = threading.Thread(target=print_square,name="Square Thread", args=(num,))
    t2 = threading.Thread(target=print_factorial,name="Factorial Thread", args=(num,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")
