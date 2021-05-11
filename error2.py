
#in this program this code will go through the error part as is consist of 'r' read type in open and still print the 'run this anyway' because of finally key!
try:
    j=open ('simple.txt','r')
    j.write("hey there jatin this side")
except IOError:
    print("Error: could not find")
finally:
    print("run this anyway!")
