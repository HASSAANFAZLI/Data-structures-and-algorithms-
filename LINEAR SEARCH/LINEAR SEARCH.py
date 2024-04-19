'''
LINEAR SEARCH,  EACH ELEMENT OF AN ARRAY IS CHECKED IN ORDER, FROM THE LOWER BOUND TO THE UPPER BOUND, UNTIL THE
ITEM IS FOUND, OR THE UPPER BOUND IS REACHED.
'''

x = [None for i in range(9)]



def intarr():
    for j in range(0, len(x)):
         item = 0
         item = int(input("enter item to store in array:"))
         x[j] = item

intarr()

found = False
a = 0

item = int(input("enter item to be found: "))

for i in range(0, len(x)):
    if item == x[i]:
        found = True
        a = i

if found == True:
    print(a)
else:
    print("no item found")