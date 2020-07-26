### write gui form to capture data
from tkinter import *


### fuction to save the info form
def save_info():
    firstname_info = firstname.get()
    second_name_info = second_name.get()
    postcode_info = str(postcode.get())
    mobile_number_info = str(mobile_number.get())
    email_info = email.get()
    job_title_info = job_title.get()
    age_info = str(age.get())
    print( firstname_info, second_name_info, postcode_info, mobile_number_info, email_info, job_title_info, age_info )


    firstname_entry.delete(0, END)
    second_name_entry.delete(0, END)
    postcode_entry.delete(0, END)
    mobile_number_entry.delete(0, END)
    email_entry.delete(0, END)
    job_title_entry.delete(0, END)
    age_entry.delete(0, END)
    
                                 
### creat text file
    file = open( "user.txt" , 'w')
    file.write( firstname_info)
    file.write( second_name_info)
    file.write( postcode_info)
    file.write( mobile_number_info)
    file.write(  email_info)
    file.write( job_title_info)
    file.write(age_info)
    file.close()
    print( " User " , firstname_info, " has been registered successfully! ")
    


screen=Tk()
screen.geometry( "500x500")
screen.title("Heaven 33 form")
heading =Label(text= "Heaven 33 sign up", bg = "gray", fg= "black", width= "500", height= "3")

## creating name lables

firstname_text =Label(text= "First name",)
second_name_text = Label(text= "Second name",)
postcode_text = Label(text= "Postcode",)
mobile_number_text = Label(text= "Mobile number",)
email_text = Label(text= "Email address",)
job_title_text = Label(text= "Job title",)
age_text =Label(text= "Age",)


###position of lables
firstname_text.place( x=10, y = 20)
second_name_text.place( x=10, y = 60)
postcode_text.place( x=10, y = 100)
mobile_number_text.place( x=10, y = 140)
email_text.place( x=10, y = 180)
job_title_text.place( x=10, y = 220)
age_text.place( x=10, y = 260)


### creating the varables...
firstname = StringVar()
second_name = StringVar()
postcode = IntVar()
mobile_number = IntVar()
email =StringVar()
job_title = StringVar()
age = IntVar()

## creating the entryies
firstname_entry = Entry(textvariable = firstname_text)
second_name_entry = Entry(textvariable = second_name)
postcode_entry = Entry(textvariable = postcode)
mobile_number_entry = Entry(textvariable = mobile_number)
email_entry = Entry(textvariable = email)
job_title_entry = Entry(textvariable = job_title)
age_entry = Entry(textvariable = age)

## placing the entry boxes


firstname_entry.place( x=10, y = 40, width= 250)
second_name_entry.place( x=10, y = 80, width =250)
postcode_entry.place( x=10, y = 120, width = 250)
mobile_number_entry.place( x=10, y = 160, width= 250)
email_entry.place( x=10, y = 200, width= 250)
job_title_entry.place( x=10, y =240, width= 250 )
age_entry.place( x=10, y = 280, width= 250)

### adding a button to register form

register = Button(screen, text = "Register", width= "33", height="2", command = save_info )
register.place(x = 10 , y= 320)











###add more


### work out how to point input boxes to data file
###write a gui with pasword access to show and list all the inside details
### work out  a program to send users their access code
