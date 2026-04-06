#import the regular expressions model
import re

#user types password and it is then stored in the password_input variable
password_input = input()

#^ starts at beginning of string
#then checks if it has at least one lowercase character
#then checks if it has at least one uppercase character
#then checks if it has at least one number
#then ensures that the string is at least 8 characters long
#then signify the end of the string
#start and end of string are signified in order to confirm that it follows these rules all through out the string
password_check = re.compile(r'''
    ^
    (?=.*[a-z]) 
    (?=.*[A-Z])
    (?=.*\d)
    .{8,}
    $
''', re.VERBOSE)
                            
#match is a variable made for using the password_check with the match regular expression function to be used on the password_input
#this is to check if the password inputted follows the requirements
match = password_check.match(password_input)

#if the password follows the rules in the password_check variable then it prints that the password is valid
if match:
    print('Valid Password')
#if the password does not follow the rules in the password_check variable then it prints that the password is not valid
else:
    print('Invalid Password')
