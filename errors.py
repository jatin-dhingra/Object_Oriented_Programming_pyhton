try:
    j=open ('simple.txt','r')
    j.write("hey there jatin this side")
except IOError:
    print("Error: could not find")
else:
    print("successfully deployed")
    j.close()
