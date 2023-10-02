'''
Title : National Id Feature data extraction

Objective:
    - load The national Id photo
    - Preprocess the Id and filter the image 
    - Make an image thersholding and making boundry's
    - Extract the text of the image 

'''
import streamlit as st
import streamlit_ext as ste
import cv2 
import pytesseract as pt
from PIL import Image
import numpy as np
from skimage.morphology import remove_small_objects
class National_Id_Data:
    def __init__(self) -> None:
        st.title("Id Information Extractor")
        st.header("please upload the national ID")
        self.tab1, self.tab2 = st.tabs(
            ["upload the National Id", "extracted data"])
        pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.IdNo=0
        pass
    @st.cache_data
    def LoadImage(_self, file):
        '''
        input: 
            file->image file 
        functionality:
            Load 
        return:
            numpy_image
        '''
        with st.spinner('Wait for it...'):
            while (file is None):
                st.stop()  # wait until loading the data
        st.success('Done✅')
        img_loaded=Image.open(file)
        img_numpy=np.array(img_loaded).astype(np.uint8)
        return  img_numpy  # return the loaded data
    
    def remove_noise(self,gray, num):
        Y, X = gray.shape
        nearest_neigbours = [[
            np.argmax(
                np.bincount(
                    gray[max(i - num, 0):min(i + num, Y), max(j - num, 0):min(j + num, X)].ravel()))
            for j in range(X)] for i in range(Y)]
        result = np.array(nearest_neigbours, dtype=np.uint8)
        return result
        
    def ImagePreprocess(self,Image):
        #apply filters to get best Image
        gray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
        gray=cv2.resize(gray,(5000,4000),cv2.INTER_AREA)
        name=gray[1100:1900,2000:5000]
        address=gray[1800:2700,2000:5000]
        Id_No=gray[2600:5000,2000:5000]
        #Masking the information of the ID
        name=cv2.inRange(name,lowerb=0,upperb=80)
        address=cv2.inRange(address,lowerb=0,upperb=80)
        Id_No=cv2.inRange(Id_No,lowerb=0,upperb=80)
        #end of the masking
        
        # gray=cv2.erode(gray,kernel=np.ones((11,11)))
        # gray=remove_small_objects(gray,10,300)
        # gray=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel=np.ones((1,1)))
        # # gray=cv2.medianBlur(gray,5)
        # # gray=cv2.erode(gray,(3,3),iterations=1)
        # # gray=cv2.dilate(gray,(3,3),iterations=1)
        # sts=str(pt.image_to_string(gray,lang="ara"))
        # st.write(sts)
        pass

    def ImageReader_InformationExtarction(self):
        with self.tab1:
            self.file = st.file_uploader(
                "Please Upload the National Id as (JPEG,PNG,JPG)",type=["png","jpg","jpeg"]
                )
            data = self.LoadImage(self.file)
            self.ImagePreprocess(data)

            
            

    def main(self):
        self.ImageReader_InformationExtarction()

if __name__=="__main__":
    web=National_Id_Data()
    web.main()