#xs = [8, 23, 45,"liscenseplate",0,9,10,0,5,9,0]
import cv2
#plate = []
#num1
#num
xs =[2, 0, 6,3,15,0,9]
boxes =[[12,3,6,8],[9,8,7,8],[58,87,6,8],[98,8,78,9],[87,8,9,3],[5,78,95,6],[85,85,87,6]]
box_plate=[]



pos =[]
for idx, x in enumerate(xs):
    if x==0:
        #print(idx, x)
        pos.append(idx)

print(pos)  # [4,7,10]


for i in range(len(pos)-1):
    #print(boxes[pos[i]][0])
    #print(boxes[pos[i+1]][0])
    # Arrange array according to the min x1 to max x1 positon of bbox liscense plate
    if boxes[pos[i]][0]< boxes[pos[i+1]][0]:
        for k in pos:
            box_plate.append(boxes[k])
    else:
        l = len(pos)
        while l >0:
            box_plate.append(boxes[pos[l-1]])
            l -= 1





print(box_plate)



'''
items = [8, 23, 45, 12, 78]

for i, item in enumerate(items, start=100):
    print(i, item)
    
    
OR
 items = [8, 23, 45, 12, 78]

for i in range(len(items)):
    print("Index:", i, "Value:", items[i])   


OR

items = [8, 23, 45, 12, 78]
counter = 0

while counter < len(items):
    print(counter, items[counter])
    counter += 1
OR
items = [8, 23, 45, 12, 78]

xerox = lambda upperBound: [(i, items[i]) for i in range(0, upperBound)]
print(xerox(5))
#    [(0, 8), (1, 23), (2, 45), (3, 12), (4, 78)]

OR
items = [8, 23, 45, 12, 78]
indices = []

for index in range(len(items)):
    indices.append(index)

for item, index in zip(items, indices):
    print("{}: {}".format(index, item))

'''