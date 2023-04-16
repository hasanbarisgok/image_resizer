import streamlit as st 
from PIL import Image
import os

class image_resizer():
    
    def __init__(self):
        
        self.select_folder()
        
        
    def select_folder(self):
        
        self.uploaded_files = st.file_uploader("Choose a file.", accept_multiple_files= True, type= ["jpg", "jpeg", "png"])
        
        if self.uploaded_files:
            if not os.path.exists('resized_images'):
                os.makedirs('resized_images')
                
        if self.uploaded_files:
            self.width = int(st.number_input("Insert the new Width"))
            st.write("The selected Width value is: ", self.width)
            
            self.height = int(st.number_input("Insert the new Height"))
            st.write("The selected Height value is: ", self.height)
                
            
            if st.button("Resize Images"):
                self.resize_images()
        
    def resize_images(self):
        
        self.folder_path = os.getcwd()
        
        self.new_folder_path = os.path.abspath(os.path.join(self.folder_path, 'resized_images'))
        
        for uploaded_file in self.uploaded_files:
            filename = uploaded_file.name
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                img = Image.open(uploaded_file)
                img = img.resize((self.width, self.height))
                
                new_filename = os.path.splitext(filename)[0] + "_new" + os.path.splitext(filename)[1]
                
                img.save(os.path.join(self.new_folder_path, new_filename))
                st.write("Resized image saved as:", new_filename)
        
        
        
        
    
abc = image_resizer()