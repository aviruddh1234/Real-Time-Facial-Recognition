from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # ==================variables====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
    
        #first img
        img = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img = img.resize((505, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=505, height=130)

        #second
        img1 = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img1 = img1.resize((505, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=505, y=0, width=500, height=130)

        #third
        img2 = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img2 = img2.resize((505, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2 )

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1005, y=0, width=505, height=130)

        #bg
        img3 = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3 )

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img , text ="STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35, "bold"),bg= "white", fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=650)

        #left label frame 
        Left_frame =  LabelFrame(main_frame, bd=2 ,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left )

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)



        #Current Course 
        current_course_frame =  LabelFrame(Left_frame, bd=2 ,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=125)

        #Department
        dep_label=Label(current_course_frame,text="Department", font =("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"), state="readonly",width=17)
        dep_combo["values"]=("Select Department","ComputerScience","Aerospace","Electrical","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=17)
        course_combo["values"] = ("Select Course", "Bachelor of Engineering", "Bachelor of Technology", "Bachelor of Science")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=17)
        year_combo["values"] = ("Select Year", "First Year", "Second Year", "Third Year", "Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=17)
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

        # Class Student Info.
        class_Student_frame  = LabelFrame(Left_frame, bd=2 ,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=260,width=720,height=295)

        #student id
        studentId_label = Label(class_Student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5,sticky=W)
        
        studentID_entry=Entry(class_Student_frame,textvariable=self.va_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = Entry(class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        classDivision_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
        classDivision_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div, font=("times new roman", 12, "bold"), state="readonly", width=17)
        div_combo["values"] = ("None", "Core", "AI","Cloud","Cybersecurity","Health Inofrmatics","Gaming")
        div_combo.current(0)
        div_combo.grid(row=1, column=1  , padx=10, pady=5,sticky=W)

        # Roll No.
        rollNo_label = Label(class_Student_frame, text="Roll No.:", font=("times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = Entry(class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10,pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=17)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5,sticky=W)


        #DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        email_entry = Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No.
        phoneNo_label = Label(class_Student_frame, text="Phone No.:", font=("times new roman", 12, "bold"), bg="white")
        phoneNo_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phoneNo_entry = Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = Entry(class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacherName_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacherName_entry = Entry(class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        #bbuttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame, text="Save",command=self.add_data, width =17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text="Update",command=self.update_data, width =17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data, width =17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data, width =17 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame 2
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1, text="Take Photo Sample", width =35 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample", width =35 ,font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame 
        Right_frame =  LabelFrame(main_frame, bd=2 ,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)

        img_right = Image.open(r"C:\Users\User\OneDrive\Desktop\project grp-62\Real-Time-Facial-Recognition\images\login.png")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right )

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
    
        #+++++Search System+++++

        Search_frame  = LabelFrame(Right_frame, bd=2 ,bg="white", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red" ,fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly", width=17)
        search_combo["values"] = ("Select", "Roll_No.", "Phone_No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        search_entry =ttk.Entry(Search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        
        search_btn=Button(Search_frame, text="Search", width =12 ,font=("times new roman",12,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3,)

        showAll_btn=Button(Search_frame, text="Reset", width =12 ,font=("times new roman",12,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0,column=4,)

        # ======Table Frame========
        table_frame  = Frame(Right_frame, bd=2 ,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.students_table=ttk.Treeview(table_frame,columns=("dep","course", "year", "sem", "Id", "name", "div", "roll","gender","dob", "email", "phone", "address", "teacher", "photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.students_table.xview)
        scroll_y.config(command=self.students_table.yview)

        self.students_table.heading("dep", text="Department")
        self.students_table.heading("course", text="Course")
        self.students_table.heading("year", text="Year")
        self.students_table.heading("sem", text="Semester")
        self.students_table.heading("Id", text="StudentId")
        self.students_table.heading("name", text="Name")
        self.students_table.heading("roll", text="Roll")
        self.students_table.heading("gender", text="Gender")
        self.students_table.heading("div", text="Division")
        self.students_table.heading("dob", text="DOB")
        self.students_table.heading("email", text="Email")
        self.students_table.heading("phone", text="Phone")
        self.students_table.heading("address", text="Address")
        self.students_table.heading("teacher", text="Teacher")
        self.students_table.heading("photo", text="PhotoSampleStatus")
        self.students_table["show"]="headings"

        self.students_table.column("dep",width=100)
        self.students_table.column("course",width=100)
        self.students_table.column("year",width=100)
        self.students_table.column("sem",width=100)
        self.students_table.column("Id",width=100)
        self.students_table.column("name",width=100)
        self.students_table.column("roll",width=100)
        self.students_table.column("gender",width=100)
        self.students_table.column("div",width=100)
        self.students_table.column("dob",width=100)
        self.students_table.column("email",width=100)
        self.students_table.column("phone",width=100)
        self.students_table.column("address",width=100)
        self.students_table.column("teacher",width=100)
        self.students_table.column("photo",width=100)

        self.students_table.pack(fill=BOTH, expand=1)
        self.students_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ===============function declaration==================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are rquired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ayuvi",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.va_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()  
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #====================fetching the data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ayuvi",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.students_table.delete(*self.students_table.get_children())
            for i in data:
                self.students_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #====================get cursor=============================
    def get_cursor(self,event=""):
        cursor_focus=self.students_table.focus()
        content=self.students_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    

    #=============update fucntion===============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are rquired",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ayuvi",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.va_std_id.get()     
                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    

    #================delete function===================
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Are you sure you want to delete the student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ayuvi",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student data successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #=================reset===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("Select ")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.va_std_id.set("")
                    
                

        



            

    
    


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()