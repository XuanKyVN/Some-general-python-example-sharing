from PIL import Image
import glob
import os

# new folder path (may need to alter for Windows OS)
# change path to your path
dest = r"C:\Users\Admin\Documents\Resizeimages\resized"
source= 'C:/Users/Admin/Documents/Resizeimages'
source_jpg = source+"/*.jpg"
new_size = 300
save_samefolder = True

# loop over existing images and resize
# change path to your path
for filename in glob.glob(source_jpg): #path of raw images
    img = Image.open(filename).resize((new_size,new_size))
    # save resized images to new folder with existing filename
    if save_samefolder:
        img.save('{}{}{}'.format(source,'/',os.path.split(filename)[1]))
    else:
        # create new folder
        if not os.path.exists(dest):
            os.makedirs(dest)
        img.save('{}{}{}'.format(dest, '/', os.path.split(filename)[1]))