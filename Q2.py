#Reading input file 
inp_file = open("input.txt", "r")
out_file = open("output.txt", "w")

#Using dictionary data structure to store key value pairs
data = {}

#Looping in the lines of input file on each word, adding / incrementing the count of the word  
for line in inp_file:
    out_file.write(line)
    split_line = line.split()
    for x in split_line:
        if(data.get(x)==None):
            data[x]=1
        else:
            data[x] += 1
            
#Looping and printing the key values            
out_file.write("\n****Word_Count****\n") 
for key, value in data.items(): 
        out_file.write('%s:%s\n' % (key, value))
#Close the files
inp_file.close()
out_file.close()