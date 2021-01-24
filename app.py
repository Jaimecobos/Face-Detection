
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

def detect(image):

    # Returning the image with bounding boxes drawn on it (in case of detected objects), and bounding box array
    return image

def about():
	st.write(
		'''
		yo
		''')


def main():
    st.title("Bread Detection App :sunglasses: ")
    st.write("**Bounding box detection using keras and tenserflow**")

    activities = ["Home", "About"]
    choice = st.sidebar.selectbox("Pick something fun", activities)

    if choice == "Home":

    	st.write("Go to the About section from the sidebar to learn more about it.")
        
        # You can specify more file types below if you want
    	image_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

    	if image_file is not None:

    		image = Image.open(image_file)

    		if st.button("Process"):
                
                # result_img is the image with rectangle drawn on it (in case there are bread detected)
                # result_faces is the array with co-ordinates of bounding box(es)
    			result_img, result_bread = detect(image=image)
    			st.image(result_img, use_column_width = True)
    			st.success("Found {} bread\n".format(len(result_bread)))

    elif choice == "About":
    	about()




if __name__ == "__main__":
    main()
