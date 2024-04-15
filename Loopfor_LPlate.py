import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
#import cvzone
from collections import Counter  # Import Counter from collections module
import glob

model = YOLO("C:/Users/Admin/PythonLession/yolo_dataset/best_plate_ky.pt")



#---------------------------------------
def findmin(marks):

# Example 1: Using for loop

    minimum_val = marks[0]
    for i in range(1, len(marks)):
        if (marks[i] < minimum_val):
            minimum_val = marks[i]

    result = marks.index(minimum_val)
    #print (result)
    #print(minimum_val)
    return result,minimum_val

#----------------------------------------
def object(frame):

    object_classes = []
    results = model.predict(frame)
    #  GPU / CPU extraction data from object
    result = results[0]
    boxes = results[0].boxes.xyxy.tolist() # (x1,y1, x2,y2)
    #print(boxes) # [ Tensorflow matrix]
    classes = results[0].boxes.cls.tolist()
    print(classes) # [0, 1, 3,9,8]
    names = results[0].names
    #print(names)
    #{0: 'LicensePlate', 1: '0', 2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8', 10: '9', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: 'I', 20: 'J', 21: 'K', 22: 'L', 23: 'M', 24: 'N', 25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S', 30: 'T', 31: 'U', 32: 'V', 33: 'W', 34: 'X', 35: 'Y', 36: 'Z'}
    confidences = results[0].boxes.conf.tolist()
    # [ 0.9,0.8, 0.98 .....]
    #annotator = Annotator(frame, line_width=2, example=str(names))
    # Loop in classes to find number of liscense plate and mark position

    cor_lp =[]
    posLP =0
    index=0
    boxes_lp=[]
    classes_lp=[]
    boxes_int=[]
    classes_number=[]
    for box in result.boxes:
        label1 = result.names[box.cls[0].item()]
        cords1 = [round(x) for x in box.xyxy[0].tolist()]
        boxes_int.append(cords1)
        #prob1 = round(box.conf[0].item(), 2)
        print("Object type: ", label1)
        #print("Probablity: ", prob1)
        #print("Cordinate: ", cords1)
        #print("_")
        object_classes.append(label1)
        if label1 == "LicensePlate":
            cor_lp =cords1
            posLP = index
            #print(cor_lp)
            #print(posLP)
            boxes_lp.append(boxes_int.pop(posLP))
            classes_lp.append(classes.pop(posLP))

            cv2.rectangle(frame, (cords1[0], cords1[1]), (cords1[2], cords1[3]), (0, 255, 0), 2)

        else:
            cv2.rectangle(frame,(cords1[0],cords1[1]),(cords1[2],cords1[3]),(255,0,0),1)
            cv2.putText(frame,label1,(cords1[0],cords1[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
            #cv2.putText(frame,str(cords1[0])+"," + str(cords1[0]),(cords1[0],cords1[1]),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
            classes_number.append(label1)
        index+=1
    #print (boxes_int)
    #print(boxes_lp)

    # Iterate through the results
    '''
    for box, cls, conf in zip(boxes, classes, confidences):
        annotator.box_label(box, names[int(cls)], (255, 42, 4))
    '''

#---------------------------------------------------------------
    boxes0=boxes
    classes0=classes

    boxes1=[]  # New List after sort
    # Example 1: Using for loop
    array1=[] # value index0 of element array in list sort
    index1=0
    classes1=[] # New Claseese

    # Extract item 1 of array in the list x1 of all bounding boxes
    for i in range(0, len(boxes_int)):
        array1.append(boxes_int[i][0])
    print(array1)

# Loop in list array items
    for i in range(0, len(boxes_int)):
        index1,value1 =findmin(array1) # find min value and index
        array1.pop(index1)  # Sort increament of array
        classes1.append(classes_number.pop(index1))
        boxes1.append(boxes_int.pop(index1))

    print("Boxes1"    )
    print (boxes1)
    print("classes1")
    print(classes1)
    posindex=0
    PosElm=[]
    for k in range(0,int(len(boxes1)/2)):
        if boxes1[2*k][1]>boxes1[2*k+1][1]:
            PosElm.append(2)
            PosElm.append(1)
        else:
            PosElm.append(1)
            PosElm.append(2)
    print(PosElm)

    # Find Index of value ==1
    index_val1 =[]
    for k in range(0,len(PosElm)):
        if PosElm[k]==1:
            index_val1.append(k)
    #print(index_val1)
    LP_line1=[]
    classes_line1=[]
    for k in index_val1:
        LP_line1.append(boxes1[k])
        classes_line1.append(classes1[k])
    print (LP_line1)
    print(classes_line1)



#-------------------------LINE 2--------------
    index_val2 = []
    for k in range(0, len(PosElm)):
        if PosElm[k] == 2:
            index_val2.append(k)
    #print(index_val2)
    LP_line2=[]
    classes_line2=[]
    for k in index_val2:
        LP_line2.append(boxes1[k])
        classes_line2.append(classes1[k])
    print (LP_line2) # Bounding Boxes of items
    print(classes_line2) # Number of Items

    cv2.putText(frame, "BIEN SO XE", (100, 100),cv2.FONT_HERSHEY_PLAIN,3,(255,255,200),2)
    pos=0
    for k in range(0, len(classes_line1)):
        cv2.putText(frame,str(classes_line1[k]),(100+pos, 150),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
        pos=pos+50
    pos = 0
    for k in range(0, len(classes_line2)):
        cv2.putText(frame, str(classes_line2[k]), (100+pos, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        pos = pos + 50
    pos=0
#  MAIN PROGRAM---------------------------------------------------
path = r'C:\Users\Admin\PythonLession\carplate\images\test\20240204_161923.jpg'
#for file in glob.glob(path):
img = cv2.imread(path)

#function
object(img)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()








'''
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