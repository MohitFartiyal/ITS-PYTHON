#Wap for currency converter
print ("Convert Rupee into Dollars")
rupeesAmount = int(input("Enter the amount in rupee"))
rsIntodollar =(rupeesAmount/84)
print(rupeesAmount,"Convert into Dollar",rsIntodollar)

print ("Convert Dollar into Rupees")
dollarAmount = int(input("Enter the amount in dollar"))
dollarIntorupee =(dollarAmount*84)
print(dollarAmount,"Convert into Rupee",dollarIntorupee)



friendname=["Pawan","Ivan","Anshu"]
print("before",friendname)
#to add new friend name in the list
friendname.append("Mohit ")
print("After",friendname)
#to add the name in specific position
friendname.insert(0,"Harsh")
print("Add name at index 0",friendname)
friendname.remove("Harsh")
print(friendname)
friendname.clear()
print(friendname)
friendname.pop(2)
print(friendname)


#To sort the list
friendname.sort()
print(friendname)

#to print element in the given list
for names in friendname:
    print(names)



#File Concept
f=open ("Mohit.txt","w")
f.write("My name is mohit , I am a MCa student")
f.close()

name=input("Enter your name")
email = input("Enter your email")
collegeName=input("Enter your college name")
data=name+email+collegeName

f=open("Mohit.txt","w")
f.write(data)
f.close()




#Calculator
 
def add(x,y):
     return x+y
 
def subtract(x,y):
     return x-y
 
def multiply(x,y):
     return x*y
 
def divide(x,y):
 return x/y

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice=input("Enter Choices(1/2/3/4)")
    if choice in('1','2','3','4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Envalid Input.Please Enter a number.")
            continue
        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
    
        elif choice =='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
            
        elif choice =='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
            
        elif choice =='4':
            print(num1,"/",num2,"=",divide(num1,num2))
    
    
    
    
    
#tuple can store multiple data and data can change
mytuple=("Evan","ANshu","Wani","Anjali","Wani")
for x in mytuple:
    print(x)
print(mytuple)
print(type(mytuple))

print(mytuple[1])

mytuple[1]="Adarsh"
print(mytuple)    




#if else 
userAge = int(input("Enter your age"))
if (userAge > 17):
    print("You are eligible for Voting")
else :
    print("You are not eligible for voting")
    gender = int(input("Enter your gender"))
age = int(input("Enter your Age"))
    
if (gender==1 and age > 17):
    print("You are eligile for  govt job")
elif(gender==2 and age>17):print("You are eligible for private job")
else:
    print("ENter you are not eligible for any job")

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if(a>b and b>c ):print("a is bigger number")
elif(b>a and a>c):print("b is bigger number")
elif(c>a and a>b):print("c is bigger number")
else:print("All Number is Same")




#Classes
class Mohit:
    age=20
    print("I am from Delhi")
    
x=Mohit()
print(x.age)

bornYear=int(input("Enter your Born Year"))
currentYear=int(input("Enter your Currnet YEar"))
class AgeCalculator:
    ageInYear=currentYear-bornYear
age= AgeCalculator()
print(age.ageInYear)