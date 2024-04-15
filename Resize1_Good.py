from PIL import Image
import glob
import os

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
def resize_all_img(source, new_size=640, samefolder=False ):
    dest = r"C:\Users\Admin\Documents\Resizeimages\resized"
    files = list_files(source)
    count=0
    for file_name in files:
        # Construct old file name
        filename, extension = os.path.splitext(file_name)
        if extension == '.jpg':
            # Do Some Task
            img = Image.open(source+"/"+ file_name).resize((new_size, new_size))
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
    dest = r"C:\Users\Admin\Documents\Resizeimages\resized"
    source_jpg = source+"/*.jpg"
    count =0
    # loop over existing images and resize
    # change path to your path
    for filename in glob.glob(source_jpg): #path of raw images
        img = Image.open(filename).resize((new_size,new_size))
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
resize_all_img(source, 300, True )