#Password Strength Checker
#Amelia Majtczak
#This program checks the strength of a user's password and gives feedback on how strong it is and how to
# improve it if the password is weak. 

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
    spec_characters = " "

    #Lenght check
    if len(password) >= 8:
        length = True
        strength += 1 
    

    # if statements to decide either password is weak, medium, or strong 
    

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)

    #If statements to print out if the password is weak, medium, or strong 
    #and give feedback on what is missing and how to improve if it is medium or weak.


    #window to present the password checker. 


#Main function call 
main()
