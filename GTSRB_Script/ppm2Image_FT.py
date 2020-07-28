import os
import numpy as numpy
import PIL
import matplotlib.pyplot as plt
import csv
import cv2
import numpy as np
class PPM2Image(object):
    
    def __init__(self,ppm_rpath,image_rpath):
        self.ppm_rpath = ppm_rpath
        self.image_rpath =image_rpath
        self.image_num =0
        self.ppm =None
        self.image =None
        self.roi =0
        self.index =0
        self.GTRSB_cvs_info = []

    # getGTSB_cvs only need to use once
    def getGTRSB_cvs(self,cvs_path):
        with open(cvs_path,"r") as cvs_file:
             GTRSB_cvs = csv.reader(cvs_file,delimiter=';')
             
             #the first row is filename
             for row in GTRSB_cvs:
                  self.GTRSB_cvs_info.append(row)

        return self.GTRSB_cvs_info

    def readppm(self):
        self.ppm = cv2.imread(self.ppm_rpath)
        self.image =self.ppm
    
    def getROI(self,index):
         #namestring = self.ppm_rpath.split("/")[-1]
         #indexnum = int((namestring[:-4].split("\\")[1].split("_")[1]))

         #num =int(namestring[:-4].split("\\")[1].split("_")[0])
         #print(num)
         #print(indexnum)
         #index = indexnum +num*30 +1
         #print(len(self.GTRSB_cvs_info))
         info  = self.GTRSB_cvs_info[index]
         roi = info[3:7]
         return roi

    def image_roi(self,roi):
        cv2.rectangle(self.image,(int(roi[0]),int(roi[1])),(int(roi[2]),int(roi[3])),(0,255,0),1)
        #print(self.image)
    
    def imagewrite(self):
        print(self.image_rpath)
        print(cv2.imwrite(self.image_rpath,self.image))

    def transform(self,index):
        self.readppm()
        roi = self.getROI(index)
        self.image_roi(roi)
        self.imagewrite()


if __name__ == "__main__":
    
    cvspath ="GT-final_test.test.csv"
    #ppmrpath ="00000.ppm"
    #imagerpath ="00000.JPG"
    images_rootpath =".\\Images/"
    images_outpath =".\\Images_test"

    for  filename in os.listdir(images_rootpath):
        cvspath = images_rootpath+filename+"//GT-"+str(filename)+".csv"
        index =1
        if(os.path.exists(images_outpath+"\\"+filename)):
            pass
        else:
            os.makedirs(images_outpath+"\\"+filename)
        for file_single in os.listdir(images_rootpath+"\\"+filename):
            
            if file_single.split(".")[1]=="ppm":
               # print(file_single)
                imagepath = images_outpath+"\\"+filename+"\\"+file_single.split(".")[0]+".jpg"
                ppmrpath = images_rootpath+filename+"\\"+file_single
               # print(imagepath)
                ppm2image = PPM2Image(ppmrpath,imagepath)
                ppm2image.getGTRSB_cvs(cvspath)
                ppm2image.transform(index)
                index+=1
    

        
        
