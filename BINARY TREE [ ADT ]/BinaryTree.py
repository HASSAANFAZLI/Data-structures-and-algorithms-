ArrayNodes = [[0] * 3 for x in range(20) ]
RootPointer = -1
FreeNode = 0

def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode

    NodeData = int(input("Enter the data: "))


    #FIRST NEED TO CHECK IS THEIR SPACE IN MY ARRAY
    if FreeNode <=19:
        #CREATE A NODE AND INITIALIZE
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        #CHECK DO YOU HAVE A ROOT VALUE
        if RootPointer == -1:
            RootPointer = 0

        else:
            Placed = False
            CurrentPointer = RootPointer

            while Placed == False:
                if NodeData < ArrayNodes[CurrentPointer][1]:


                    if ArrayNodes[CurrentPointer][0] == -1:
                        ArrayNodes[CurrentPointer][0] = FreeNode
                        Placed = True

                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][0]


                else:
                    if ArrayNodes[CurrentPointer][2] == -1:
                        ArrayNodes[CurrentPointer][2] = FreeNode
                        Placed = True

                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][2]



        FreeNode = FreeNode + 1

    else:
        print("binary tree is out of space")



def SearchNode():
    global ArrayNodes
    global RootPointer

    SearchData = int(input("Enter data to be searched: "))

    currentPointer = RootPointer

    while currentPointer != -1 and ArrayNodes[currentPointer][1] != SearchData:
        if SearchData < ArrayNodes[currentPointer][1]:
            currentPointer = ArrayNodes[currentPointer][0]

        else:
            currentPointer = ArrayNodes[currentPointer][2]



    print(currentPointer)







