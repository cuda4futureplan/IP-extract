# importing the module
import re

# opening and reading the file
with open('2222-9.txt') as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
lst=[]

# extracting the IP addresses
for line in fstring:
    #print(line)
    #print(pattern.search(line))
    if(pattern.search(line)!=None):
        open("ip-2222-ssh","a+").write(pattern.search(line)[0]+'\n')
        lst.append(pattern.search(line)[0])
        lst.append('\n')

# displaying the extracted IP addresses
print(lst)

