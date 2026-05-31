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
    spec_characters = "!@#$%^&*()-=+[]{}/?,.<>\|*.`~;:'"
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

    password = input("Enter your password: ")
    strength = check_password_strength(password)

    #If statements to print out if the password is weak, medium, or strong 
    if strength[0] <= 2:
        print("Your password is weak.")
    elif strength[0] <= 4:
        print("Your password is medium strength.")
    else:
        print("Your password is strong.")
    #and give feedback on what is missing and how to improve if it is medium or weak. (If statements)
    if strength[1] == False:
        print("Your password is missing an uppercase letter.")
    if strength[2] == False:
        print("Your password is missing a lowercase letter.")
    if strength[3] == False:
        print("Your password is missing a number.")
    if strength[4] == False:
        print("Your password is missing a special character.")
    if strength[5] == False:
        print("Your password is too short.")
    

    


#Main function call 
main()
