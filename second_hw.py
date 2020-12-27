# i=0
k=0
info=[]
# for i in range(2): # how many people we want to ask according to thhat, we can activate for and i then we can take more people infos
name=input("enter name: ")
surname=input("enter surname: ")
age=int(input("enter age:  "))
birth=int(input("enter birt year : "))
  
info.append(name)
info.append(surname)
info.append(age)
info.append(birth)
print("\n")
    
for k in info:
    print(k)

    
print(info) 
print("\n")

if age<18:
    print("you can't go out because it's too dangerous")
else:
    print("you can go out to the street")

    
if age == 2020-birth:
    print("birthday and age are matched!!! ")
else:
    print("birthday and age aren't matched!!! XXXXX")

print("\n")
   