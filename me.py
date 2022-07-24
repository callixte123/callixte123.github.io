# print("course")
# name="callixte is bitch" 
# print(name)
# print(len(name)) 
# print(name[0])
# #print(name[len(name)])
# #How would I print the last ! Mark in my_string variable
# print(name[len(name) - 1])
# print(name[-1])
# print(name[1:7])
# print(name[0:7:2])
# print(name[13:2:-1])
# print(name[17:0:-2])
# print(name[:])
# print(name[:: -1])


doc=input("enter some thing")
count = 0; 
print(len(doc)) 
#Counts each character except space  
for i in range(0, len(doc)):  
    if(doc[i] != ' '):  
        count = count + 1;  
print(doc)
print(count) 



# num1=int(input("enter a number"))
# num2=int(input("enter 2nd number" ))
# print("add",num1+num2)


string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)