#Password Strength Checker
#Amelia Majtczak
#This program checks the strength of a user's password and gives feedback on how strong it is and how to
# improve it if the password is weak. 

#importing module for window
from tkinter import * 



def check_password_strength(password):
    strength = 0 
    upper_l = False
    lower_l = False
    number = False
    special_char = False
    length = False


    #Upper letter check
    for letter in password:
        if letter.isupper():
            strength += 1 
            upper_l = True
            break 

    #Lower letter check
    for letter in password:
        if letter.islower():
            strength += 1 
            lower_l = True
            break

    #Number check
    for char in password:
        if char.isdigit():
            strength += 1 
            number = True
            break

    #Special character check 
    spec_characters = "!@#$%^&*()-=+[]"
    for char in password:
        for s in spec_characters:
            if char == s:
                strength += 1
                special_char = True
                break
    
    #Lenght check
    if len(password) >= 8:
        length = True
        strength += 1 
    
    return strength, upper_l, lower_l, number, special_char, length


def main():

    #window to present the password checker. 
    window = Tk()

    #Window configurations
    window.title("Password Strength Checker")
    window.geometry("1000x500")
    icon = PhotoImage(file="password security.png")
    window.iconphoto(True, icon)

        

    def enter_password(entry_password, label_feedback):
        password = entry_password.get()

        strength = check_password_strength(password) 

        feedback = ""
        feedback_s = ""
        
        
        #If statements to print out if the password is weak, medium, or strong 

        if strength[0] <= 2:
            feedback_s += "Your password is weak.\n"
            color_s = 'red'
        elif strength[0] <= 4:
            feedback_s += "Your password is medium strength.\n"
            color_s = 'orange'
        else:
            feedback_s += "Your password is strong.\n"
            color_s = 'green'

        #and give feedback on what is missing and how to improve if it is medium or weak. (If statements)

        if strength[1] == False:
            feedback += "Your password is missing an uppercase letter.\n"
            color = 'red'
        if strength[2] == False:
            feedback += "Your password is missing a lowercase letter.\n"
            color = 'red'

        if strength[3] == False:
            feedback += "Your password is missing a number.\n"
            color = 'red'

        if strength[4] == False:
            feedback += "Your password is missing a special character.\n"
            color = 'red'

        if strength[5] == False:
            feedback += "Your password is too short.\n"
            color = 'red'

        label_feedback_s.config(text = feedback_s, fg = color_s)
        label_feedback.config(text = feedback, fg = color)
        

    #entry window to enter the password
    entry_password = Entry(window,font = ("Arial",16))
    entry_password.place(x = 500, y=250, anchor = "center")
   

    #button to enter the password (used lambda to pass the entry and label as arguments to the function)
    button = Button(window, text = "Enter Password", command = lambda: enter_password(entry_password, label_feedback))
    button.place(x = 500, y = 300, anchor = "center")
    

    #label -> title 
    label_title = Label(window, text = "Password Strength Checker", font = ("Arial",24))
    label_title.place(x=500, y=140, anchor = "center")
    

    #label -> says "Enter your password to check its strength"
    label_intructions = Label(window, text = "Enter your password to check its strength", font = ("Arial",16))
    label_intructions.place(x=500, y=200, anchor = "center")
    


    #label -> feedback on the strength of the password 
    label_feedback_s = Label(window, text = "", font = ("Arial",10))
    label_feedback_s.place(x=500, y=350, anchor = "center")
    

    #label -> feedback on what is missing 
    label_feedback = Label(window, text = "", font = ("Arial",10))
    label_feedback.place(x=500, y=400, anchor = "center")  
    

    #printing the mouse position for tesitng. 

    #def show_mouse_position(event):
        #print(event.x, event.y)

    #window.bind('<Motion>', show_mouse_position)


    window.mainloop()


#Main function call 
main()
