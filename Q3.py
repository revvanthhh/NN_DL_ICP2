height_inp = input("Enter height in inches: ")
#Taking inputs and splitting 
heights = height_inp.split()
heights_list = []
#Looping through the input, converting heights from inches to centimeters and appending it in a list
for height in heights:
    value = int(height)
    heights_list.append(value*2.54)
#Printing the list    
print("Heights in centimeters : ",heights_list)
