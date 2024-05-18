class node:
    def __init__(self, datap, nextnodep):
        self.Data = datap
        self.Pointer = nextnodep

#DECLARE LINKLIST : ARRAY[0:9] OF node

LinkList = [node(1,1), node(5,4),node(6,7), node(7, -1), node(2, 2), node(0,6), node(0,8), node(56, 3),node(0,9), node(0, -1) ]

StartPointer = 0
emptyList = 5


def addnode(currentpointer):
    global LinkList
    global emptyList

    data = int(input("enter the data to add: "))

    #CHECKING LINKLIST IF FULL OR NOT
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        #increment emptylist pointer after storing it in a temporary variable
         freelist = emptyList

         emptyList = LinkList[emptyList].Pointer

         newnode = node(data, -1)

         LinkList[freelist] = newnode

         while currentpointer != -1:
             previouspointer = currentpointer
             currentpointer = LinkList[currentpointer].Pointer


         LinkList[previouspointer].Pointer = freelist


         return True



def deleteNode():
    global emptyList
    global LinkList
    global StartPointer

    currentpointer = StartPointer

    datatoremove = int(input("enter data to remove: "))

    # SEARCHING THE INDEX OF THE ELEMENT THAT YOU WANT TO REMOVE
    previoispointer = 0
    while currentpointer != -1 and LinkList[currentpointer].Data != datatoremove:
        previoispointer = currentpointer
        currentpointer = LinkList[currentpointer].Pointer


    if currentpointer == -1:
        return False

    else:
        if StartPointer == currentpointer:
            StartPointer = LinkList[StartPointer].Pointer

        else:
            LinkList[previoispointer].Pointer = LinkList[currentpointer].Pointer


        LinkList[currentpointer].Data = 0
        LinkList[currentpointer].Pointer = emptyList
        emptyList = currentpointer
        return True



def outputNodes():
    global LinkList
    global StartPointer
    currentpointer = StartPointer
    while currentpointer != -1:
        print(str(LinkList[currentpointer].Data))
        currentpointer = LinkList[currentpointer].Pointer



def Search():
    global LinkList
    global StartPointer

    currentpointer = StartPointer

    data = int(input("Enter the data to be searched: "))

    while currentpointer != -1:
        if LinkList[currentpointer].Data == data:
            return currentpointer
        else:
            currentpointer = LinkList[currentpointer].Pointer

    return currentpointer


def addinginorder():
    global LinkList
    global StartPointer
    global emptyList

    data = int(input("enter data to be entered"))

    newnode = node(data,-1)

    if emptyList < 0 or emptyList > 9:
        return False

    else:
        currentpointer = StartPointer
        freelist = emptyList
        emptyList = LinkList[emptyList].Pointer

        LinkList[freelist] = newnode

        while currentpointer != -1 and data > LinkList[currentpointer].Data:
            previouspointer = currentpointer
            currentpointer = LinkList[currentpointer].Pointer


        if currentpointer == StartPointer:
            LinkList[freelist].Pointer == StartPointer
            StartPointer = freelist

        else:
            LinkList[previouspointer].Pointer = freelist
            LinkList[freelist].Pointer = LinkList[previouspointer].Pointer



