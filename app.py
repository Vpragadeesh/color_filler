import numpy as np
import cv2
import os
import streamlit as st
from PIL import Image

def colorizer(image):
    # Paths to load the model
    DIR = "/Users/addhithyarh/Colorizer"
    PROTOTXT = os.path.join(DIR, "models/models_colorization_deploy_v2.prototxt")
    POINTS = os.path.join(DIR, "models/pts_in_hull.npy")
    MODEL = os.path.join(DIR, "models/colorization_release_v2.caffemodel")

    # Load the Model
    print("Loading model...")
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    pts = np.load(POINTS)

    # Load centers for ab channel quantization used for rebalancing.
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    # Convert image to grayscale and then to RGB
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    scaled = img.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)

    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    print("Colorizing the image...")
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    ab = cv2.resize(ab, (img.shape[1], img.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2RGB)
    colorized = np.clip(colorized, 0, 1)

    colorized = (255 * colorized).astype("uint8")

    return colorized

st.write("# Colorize your Black and white image")
st.write(" This is an app to Colorize your B&W images.")

file = st.sidebar.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    img = np.array(image)
    
    st.text("Your original image")
    st.image(image, use_column_width=True)
    
    st.text("Your colorized image")
    color = colorizer(image)
    
    st.image(color, use_column_width=True)
    
    print("done!")
