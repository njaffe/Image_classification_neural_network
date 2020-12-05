import streamlit as st

# YOLO object detection
import cv2 as cv
import numpy as np
import time
from PIL import Image

################################################################################

WHITE = (255, 255, 255)
img = None
img0 = None
outputs = None

################################################################################

# Load names of classes and get random colors
    # classes = open('coco.names').read().strip().split('\n')

classes = open('classes.txt').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

# Give the configuration and weight files for the model and load the network.
# net = cv.dnn.readNetFromDarknet('yolov3_CUSTOM.cfg', 'FIRST_TRAIN_yolov3_CUSTOM_last.weights')

### Retrained!
net = cv.dnn.readNetFromDarknet('yolov3_CUSTOM.cfg', 'yolov3_CUSTOM_last.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

# determine the output layer
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

################################################################################

### Functions

# def load_image(path):
def load_image(img_array):
    # st.write('Loading image...')
    global img, img0, outputs, ln

    # img0 = cv.imread(path) # change this to work with output of streamlit file uploader

    img0 = img_array

    img = img0.copy()

    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time() - t0

    # combine the 3 output groups into 1 (10647, 85)
    # large objects (507, 85)
    # medium objects (2028, 85)
    # small objects (8112, 85)
    outputs = np.vstack(outputs)
    post_process(img, outputs, 0.5)
    st.image(img.astype(np.uint8))


def post_process(img, outputs, conf):
    # st.write('Post-processing...')
    H, W = img.shape[:2]

    boxes = []
    confidences = []
    classIDs = []

    for output in outputs:
        scores = output[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > conf:
            x, y, w, h = output[:4] * np.array([W, H, W, H])
            p0 = int(x - w//2), int(y - h//2)
            p1 = int(x + w//2), int(y + h//2)
            boxes.append([*p0, int(w), int(h)])
            confidences.append(float(confidence))
            classIDs.append(classID)
            # cv.rectangle(img, p0, p1, WHITE, 1)

    indices = cv.dnn.NMSBoxes(boxes, confidences, conf, conf-0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            st.write(classes[classIDs[i]], confidences[i])

def trackbar(x):
    global img
    conf = x/100
    img = img0.copy()
    post_process(img, outputs, conf)
    cv.displayOverlay('window', f'confidence level={conf}')
    cv.imshow('window', img)

################################################################################

### Streamlit background image and titles

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('/users/noah/Github_repos/Project_5/background_image.png')

st.title('Intertidal Organism Detection App')
st.text('Built with Streamlit, Yolov3 and OpenCV')
st.text('Background image: https://www.worldatlas.com/articles/what-is-the-intertidal-zone.html')
st.text('Background code: https://discuss.streamlit.io/t/how-do-i-use-a-background-image-on-streamlit/5067/3')
st.write('**********************************************************************')

################################################################################

### User upload and model

st.write(
'''
Intertidal invert image
'''
)

# img_file_buffer = st.file_uploader('upload')
img_file_buffer = st.file_uploader("Upload Image",type=['jpg', 'jpeg'])

### Dealing with PNG
# st.write(img_file_buffer.name)

# if img_file_buffer.name.endswith('.png'):
#     our_image = Image.open(img_file_buffer)
#     our_image.save(img_file_buffer.name.replace('png','.jpg'))



if img_file_buffer is not None:
    our_image = Image.open(img_file_buffer)
    st.text('Original Image')
    st.image(our_image)


if st.button("Identify"):
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    load_image(img_array)
    # st.write('did it!')





################################################################################
