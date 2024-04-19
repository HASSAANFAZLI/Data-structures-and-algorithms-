'''
STACK ADT
USES LIFO [ LAST IN FIRST OUT ]
'''

stack = [None for i in range(9)]
basepointer = 0
toppointer = -1
lenstack = len(stack) - 1
popitem = None
choice = 0



def intial():
    for x in range(9):
        stack[x] = ''


def push(item):
    global  toppointer, lenstack
    if toppointer < lenstack:
        toppointer = toppointer + 1
        stack[toppointer] = item
    else:
        print("stack if full, cannot push")


def pop():
    global basepointer, toppointer, popitem, lenstack
    if toppointer == -1:
        print("stack is empty")
    else:
        popitem = stack[toppointer]
        stack[toppointer] = ''
        toppointer = toppointer - 1
    return popitem


def displayStack():
    global toppointer
    for i in range(8, -1, -1):
        if i == toppointer:
            print(stack[i], '\t<---')
        else:
            print(stack[i])


while choice != 5:
    print("   ")
    print("1 - intialisation")
    print("2 - push")
    print("3 - pop")
    print("4 - display")
    print("5 - exit")
    choice = int(input("enter choice: "))
    if choice == 1:
        intial()
    elif choice == 2:
        item = int(input("enter item to be added in stack: "))
        push(item)
    elif choice == 3:
        pop()
        
    elif choice == 4:
        displayStack()
    elif choice == 5:
        break
