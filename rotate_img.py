from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

#----------------

from PIL import Image, ImageDraw, ImageFont

def draw_boxes_on_image(image_path):
    """
    data: [x1, y1, x2, y2, confidence, label] list
    """
    image = Image.open(image_path)

    # Run the inference and retrieve the boxes
    results = model(image)
    predictions = results[0].boxes.data.tolist()

    label_names = ["ID CARD", "PASSPORT"] # Change if needed
    colors = ["orange", "blue"] # Change if needed

    draw = ImageDraw.Draw(image)
    font_path = "SpaceMono-Regular.ttf" # Change if needed
    font = ImageFont.truetype(font=font_path, size=24)

    for prediction in predictions:
        x1, y1, x2, y2, confidence, label = prediction
        label = int(label)
        # Draw the box
        draw.rectangle([(x1, y1), (x2, y2)], outline=colors[label], width=5)

        # Draw the text with the label name and confidence
        text = f"{label_names[label]} ({confidence:.3f})"
        text_width, text_height = font.getsize(text)
        text_x = x1 + 5
        text_y = y1 + 5
        draw.rectangle([(text_x, text_y), (text_x + text_width, text_y + text_height)], fill=colors[label])
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

    return image

image_with_boxes = draw_boxes_on_image("pic/passport.jpg")
image_with_boxes.show()


#----------------------
import numpy as np
def retrieve_documents_from_image(image_path):
    results = model(image_path)
    predictions = results[0].boxes.data.tolist()

    im = Image.open(image_path)
    im = np.array(im)

    docs = []

    for prediction in predictions:
        pred_class = int(prediction[-1])
        x1, y1, x2, y2 = prediction[:4]
        docs.append((im[int(y1):int(y2), int(x1):int(x2)], pred_class))

    return docs



import cv2
def compare_white_pixels(image):
    """
    Returns True if the left half of image
    has more white pixels than the right half

    Parameters:
        image : np.ndarray
    """

    width = image.shape[1]
    left_region = image[:, :int(width / 2)]
    right_region = image[:, int(width / 2):]

    left_white_pixels = np.sum(left_region == 255)
    right_white_pixels = np.sum(right_region == 255)

    return left_white_pixels > right_white_pixels


def rotate_if_necessary(image):
    """
    Resets an image that has been rotated 90°/180°/270°.

    Parameters
        image : np.ndarray
    """

    # Reset image to horizontal position if necessary
    if image.shape[0] > image.shape[1]:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Convert image to grayscale
    image_binary = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply some Gaussian blur and then Otsu's thresholding
    image_binary = cv2.GaussianBlur(image_binary, (5, 5), 0)
    _, image_binary = cv2.threshold(image_binary, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Rotate image by 180° if necessary
    if not compare_white_pixels(image_binary):
        image = cv2.rotate(image, cv2.ROTATE_180)

    return image
#--------------------------------------------------------
image_path = "pic/passport.jpg"
docs = retrieve_documents_from_image(image_path)
document = rotate_if_necessary(docs[0])

import matplotlib.pyplot as plt
plt.axis("off")
plt.imshow(document) # Display the document
plt.imsave("id_doc.jpg", document) # Save the document