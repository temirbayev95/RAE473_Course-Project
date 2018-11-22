##Author CROMBEZ Maxime
##Group 1
import os

SE= input("Enter your OS IOS/Linux/Windows:")
w=str("Windows")
name= input("Name of the file: ")
os.system("echo > " + str(name)+".txt")
nb=input("Enter the iteration number :")
pop = input("Enter your IP ADDRESS : ")
print("Loading...")

if SE==w:
    print("OK Windows")
    test = open(str(name)+".txt", "w")
    test.close()
    os.system("ping " + str(pop)+" -n "+ str(nb)+" >> " + str(name)+".txt")
else:
    print("OK IOS")
    test=open(str(name)+".txt", "w")
    test.close()
    os.system("ping " + str(pop)+" -c "+str(nb)+" >> " + str(name)+".txt")
    
print("End")
print("Your file is ready")

