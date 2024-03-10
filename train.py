from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root , text ="TRAINING THE DATASET", font = ("times new roman", 45, "bold"),bg= "white", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top )

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font = ("times new roman", 30, "bold"),bg= "darkblue", fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom )

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)
    
    def train_classifier(self):
        data_dir=(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehension 

        faces=[]  #created a list for faces
        ids=[]    #created a list for ids

        for image in path:
            img=Image.open(image).convert('L') #converting into grayscale image
            imageNp=np.array(img,'uint8') #uint8 is a datatype 
            id=int(os.path.split(image)[1].split('.')[1]) #splitted the image path to get the ids 

            faces.append(imageNp)  #appended the faces into the face list 
            ids.append(id)     #appended the ids into the ids list 
            cv2.imshow("Training",imageNp) 
            cv2.waitKey(1)==13
        ids=np.array(ids)  # creted a numpy array for the ids 

        #=================== Train the classifier and save====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")  #trained file is written into classifer.xml
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","data training completed successfully !!!")





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()