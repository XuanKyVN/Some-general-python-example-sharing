import cv2

marrtrix = [82, 31, 40, 78, 90, 3, 120]

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

idx,value =findmin(marrtrix)
print(idx)
print(value)


frame = cv2.imread("testpic.png")


#------------------------------------------------------------------
marks1 = [[44,53, 731, 735], [121,100,252,330],[331,124,445,324],[503,98,624,340],[122,450,251,695],[344,464,485,674],[549,444,677,675]]
for i in range(0,len(marks1)):
    cv2.rectangle(frame,(marks1[i][0],marks1[i][1]),(marks1[i][2],marks1[i][3]),(255,0,0),1)

frame = cv2.resize(frame,(640,640))
classes=[0,5,8,9,2,4,12]

marks2=[]  # New List after sort
# Example 1: Using for loop
array1=[] # value index0 of element array in list
#array2=[]
classes2=[] # New Claseese

# Extraxt item 1 of array in the list
for i in range(0, len(marks1)):
    array1.append(marks1[i][0])
print(array1)

# Loop in list array items
for i in range(0, len(marks1)):
    index1,value1 =findmin(array1) # find min value and index
    array1.pop(index1)
    #array2.append(value1)   #
    classes2.append(classes.pop(index1))
    marks2.append(marks1.pop(index1))
print (marks2)
print(classes2)

array3_x=[]
array3_y=[]
for i in range(1, len(marks2)):
    array3_x.append(marks2[i][0]-marks2[0][0])
    array3_y.append(marks2[i][1] - marks2[0][1])
print(array3_x)
print(array3_y)




'''
array4=[]
for i,j in zip(array3_x,array3_y):
    array4.append(abs(i-j))
print(array4)
'''
'''
list1.remove(item)
list1.insert(new_index, item)
OR
old_index = list1.index(item)
list1.insert(new_index, list1.pop(old_index))

'''








cv2.imshow("display",frame)
cv2.waitKey(0)