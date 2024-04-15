from PIL import Image
import glob
import os,cv2

# new folder path (may need to alter for Windows OS)
# change path to your path

source= 'C:/Users/Admin/Documents/Resizeimages'
new_size=640

save_samefolder = False

def list_files(dir_path):
    # list to store files
    res = []
    try:
        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file_path)):
                res.append(file_path)
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    return res

def check_image_size(img_path,resize_val):
    img =cv2.imread(img_path)
    h,w,c =img.shape
    print(img.shape)
    newresize_h=0
    newresize_w=0

    if h>w:
        #print("h>w")
        if resize_val > h:
            #print("h<resize val")
            a = (resize_val - h) / h  # check % reduce size for example h=640,w=400, resize =500. a =(640-500)/640 =0.21875
            newresize_h = resize_val
            # print(a)
            newresize_w = w + int(w * a)
        elif resize_val < h and resize_val > w:
            #print("resize val<h or h <resize val< w")
            a = (h-resize_val) / h  # check % increase size
            newresize_h = resize_val
            print(a)
            newresize_w = w - int(w * a)

        else:  # resize <h and width
            print("resize val<h and <w")
            a = (h - resize_val) / h  # check % increase size
            newresize_h = resize_val
            print(a)
            newresize_w = w - int(w * a)

    elif w>h:
        print("w>h")
        if resize_val > w:
            print("h<resize val")
            a = (resize_val - w) / w  # check % reduce size for example h=640,w=400, resize =500. a =(640-500)/640 =0.21875
            newresize_w = resize_val
            # print(a)
            newresize_h = h + int(h * a)
        elif resize_val<w and resize_val>h:
            print("resize val<h or h <resize val< w")
            a = (w-resize_val) / w  # check % increase size
            newresize_w = resize_val
            print(a)
            newresize_h = h - int(h * a)

        else: # resize <h and width
            print("resize val<h and <w")
            a = (w-resize_val) / w  # check % increase size
            newresize_w = resize_val
            print(a)
            newresize_h = h - int(h * a)
    else:
        newresize_w = resize_val
        newresize_h =resize_val

    #print ("width new: "+ str(newresize_w))
    #print("height new: " +str(newresize_h))
    return newresize_w,newresize_h


def resize_all_img(source, new_size=640, samefolder=False ):
    dest = source+"/resized"
    files = list_files(source)
    count=0

    for file_name in files:
        # Construct old file name
        new_width, new_height = check_image_size(source+"/"+ file_name, new_size)
        print("new width:" +str(new_width))
        print("new Height: " +str(new_height))
        filename, extension = os.path.splitext(file_name)
        if extension == '.jpg':
            # Do Some Task
            img = Image.open(source+"/"+ file_name).resize((new_width, new_height))
            # save resized images to new folder with existing filename
            if samefolder:
                img.save('{}{}{}'.format(source,'/',file_name))
                count+=1
            else:
                # create new folder
                if not os.path.exists(dest):
                    os.makedirs(dest)
                img.save('{}{}{}'.format(dest, '/', file_name))
                count += 1
    print( str(count) + " files have been resized")



def resize_all_img_1(source, new_size=640, samefolder=False ):
    dest = source+"/resized"
    source_jpg = source+"/*.jpg"
    count =0
    # loop over existing images and resize
    # change path to your path
    for filename in glob.glob(source_jpg): #path of raw images

        new_width, new_height = check_image_size(source+"/"+ os.path.split(filename)[1], new_size)

        img = Image.open(filename).resize((new_width,new_height))
        # save resized images to new folder with existing filename
        if samefolder:
            img.save('{}{}{}'.format(source,'/',os.path.split(filename)[1]))
            #print(os.path.split(filename)[1])
            count += 1
        else:
            # create new folder
            if not os.path.exists(dest):
                os.makedirs(dest)
            img.save('{}{}{}'.format(dest, '/', os.path.split(filename)[1]))
            count+=1
    print(str(count) + " files have been resized")




resize_all_img(source, 800, False )

#pathtest = r"C:\Users\Admin\Documents\test\crop_img_227.jpg"
#w,h = check_image_size(pathtest,900)
#print(w)
#print(h)
