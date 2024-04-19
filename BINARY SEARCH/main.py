'''
A BINARY SEARCH IS MORE EFFICIENT IF A LIST IS ALREADY SORTED. THE VALUE OF THE MIDDLE ITEM IN THE LIST IS FIRST
TESTED TO SEE IF IT MATCHES THE REQIURED ITEM, AND THE HALF OF THE LIST THAT DOES NOT CONTAIN THE REQUIRED ITEM
IS DISCARDED. THEN, THE NEXT ITEM OF THE LIST TO BE TESTED IS THE MIDDLE ITEM OF THE HALF LIST THAT WAS KEPT. THIS
IS REPEATED UNTIL THE REQUIRED ITEM IS FOUND OR THERE IS NOTHING LEFT TO TEST.
'''

myLIST = [None for i in range(9)]

def intiarr():
    for i in range(0, 9):
        item = 0
        item = int(input("enter item to be add: "))
        myLIST[i] = item

intiarr()

myLIST = sorted(myLIST)
print(myLIST)

found = False
lb = 0
up = len(myLIST) - 1
item = ""
sav = 0

item = int(input("enter item to be found: "))

while (found == False) or (lb != up):
    index = int((up + lb) / 2)
    if item == myLIST[index]:
        found = True
        sav = index
    elif item > myLIST[index]:
        lb = index + 1
    elif item < myLIST[index]:
        up = index - 1

if found == True:
    print("found item at: ",sav)
else:
    print("no item in array")