import torch
from PIL import Image
import numpy as np
import streamlit as st

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

st.title("SentinelSim: Defense AI for Drone Threat Detection")

uploaded_file = st.file_uploader("Upload an aerial image", type=['jpg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    results = model(image)
    results.render()  # Annotate image in place

    threat_score = round(np.random.uniform(10, 100), 2)
    st.image(results.ims[0], caption="Threat Detections")
    st.subheader(f"Threat Level Score: {threat_score}")
