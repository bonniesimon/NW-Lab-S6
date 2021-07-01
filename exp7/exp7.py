import multiprocessing

def square_list(mylist, result, square_sum):
	
	# append squares of mylist to result array
	for idx, num in enumerate(mylist):
		result[idx] = num * num

	square_sum.value = sum(result)

	print("Result(in process p1): {}".format(result[:]))

	print("Sum of squares(in process p1): {}".format(square_sum.value))

def square_list2(mylist, q):
    for num in mylist:
        q.put(num * num)
  
def print_queue(q):
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")

def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()

def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))

if __name__ == "__main__":
    while(1):
        choice = int(input("\nEnter your choice : \n1 - IPC using Shared Memory\n2 - IPC using Message Queue\n3 - IPC using PIPES\n4. Exit\n> "))
        if (choice == 1):
            # input list
            mylist = [1,2,3,4]

            print("The following Array is going to simulate the shared memory")
            for item in mylist:
                print(item, end=" ")
            print()

            # creating Array of int data type with space for 4 integers
            result = multiprocessing.Array('i', 4)

            # creating Value of int data type
            square_sum = multiprocessing.Value('i')

            # creating new process
            p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

            # starting process
            p1.start()

            # wait until process is finished
            p1.join()

            # print result array
            print("Result(in main program): {}".format(result[:]))

            # print square_sum Value
            print("Sum of squares(in main program): {}".format(square_sum.value))
        elif (choice == 2):
            # input list
            mylist = [1,2,3,4]

            print("The following Array is going to simulate the Message Queue")
            for item in mylist:
                print(item, end=" ")
            print()

            # creating multiprocessing Queue
            q = multiprocessing.Queue()
        
            # creating new processes
            p1 = multiprocessing.Process(target=square_list2, args=(mylist, q))
            p2 = multiprocessing.Process(target=print_queue, args=(q,))
        
            # running process p1 to square list
            p1.start()
            p1.join()
        
            # running process p2 to get queue elements
            p2.start()
            p2.join()
        elif (choice == 3):
            # messages to be sent
            msgs = ["First", "second", "third?", "END"]
        
            # creating a pipe
            parent_conn, child_conn = multiprocessing.Pipe()
        
            # creating new processes
            p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
            p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
        
            # running processes
            p1.start()
            p2.start()
        
            # wait until processes finish
            p1.join()
            p2.join()
        elif (choice == 4):
            print("> > > Exiting program < < < ")
            break
        else:
            print("Invalid option")
            print("> > > Exiting program < < < ")
            break