'''
QUEUE ADT , USES THE CONCEPT OF FIFO.
'''

queue = [None for x in range(10)]
frontpointer = 0
rearpointer = 0
lenQue = len(queue)
quelen = 0
quefull = 9


def initial():
    for i in range(0,9):
        queue[i] = ''


def enqueue(val):
    global frontpointer, rearpointer, lenQue, quelen, quefull

    if quelen < quefull:
        if rearpointer < lenQue -1:
            rearpointer = rearpointer + 1
        else:
            rearpointer = 0
        quelen = quelen + 1
        queue[rearpointer] = val
    else:
        print("queue is full")



def dequeue():
    global frontpointer, rearpointer, lenQue, quelen, quefull
    item = ''
    if quelen == 0:
        print("queue is empty")

    else:
        item = queue[frontpointer]
        if frontpointer == lenQue - 1:
            frontpointer = 0
        else:
            frontpointer = frontpointer + 1
        quelen = quelen - 1


def display():
    for i in range(0, 9):
        if i == frontpointer:
            print(queue[i],'\t<---')
        elif i == (rearpointer - 1):
            print(queue[i], '\t<---')
        else:
            print(queue[i],'\t')


choice = 0
while choice !=5:
     print("1 - intialistaion of queue")
     print("2 - enqueue")
     print("3 - dequeue")
     print("4 - display")
     print("5 - exit")
     choice = int(input("enter choice: "))
     if choice == 1:
         initial()
     elif choice ==2:
         val = int(input("enter value: "))
         enqueue(val)
     elif choice ==3:
         dequeue()
     elif choice ==4:
         display()
     elif choice ==5:
         break