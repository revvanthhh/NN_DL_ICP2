#Taking input from the user
first_name = input("Enter first name :")
last_name = input("Enter last name :")
#Creating a function concatenating first name and last name
def set_fullname(fname,lname):
    full_name = fname + " " + lname
    return full_name

#Creating funtion for printing alternative charatcers in a string
def string_alternative(alt_string):
    resultant_string = alt_string[::2]
    print("Alternative characters in the string :"+resultant_string)

#Calling the function
fullnm = set_fullname(first_name,last_name)
print("Full name is : "+fullnm)
string_alternative(fullnm)