import base64
import random
import string #Importing needed libraries of Python for tasks.

def base64_encode(text): #Defining a text encryption function using base64 with an output argument that will act as a variable in the function.

    text = text.encode() #Changing the output argument from string to a type that allows encoding.
    code_b64 = base64.b64encode(text) #Base64 encryption with imported module.
    print(code_b64) #Printing the result.

base64_encode('losowehaslo123') #Result of function.



def passwordGenerator(): #A function that creates a secure password using the syntax of uppercase and lowercase letters, special characters and digits.The function takes no arguments.


    length = random.randint(10,20) #Specifying the password length in the range from 10 to 20. Applying a random option in this range using the imported random module.

    string_pwd = string.ascii_letters + string.digits + string.punctuation #Combines three sets of characters into a single character string, containing lowercase and uppercase letters, special characters, and digits. The imported string module allows us to predefine a string of characters.

    password = ''.join(random.choice(string_pwd) for i in range(length)) #Defining the password variable to which a randomly selected character is appended from the previously defined string_pwd character set without additional separators between them, the number of loops of appending characters to the password variable is equal to the length variable.

    return password #Returning a variable.
    

print(passwordGenerator()) #Result of function.
