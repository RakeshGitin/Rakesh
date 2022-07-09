
print("--HOSPITAL EMPLOYEE Activity --- " )
print("----------------MENU---------------")
print(" 1 --to create details of employee")
print(" 2 --to read details of employee")
print(" 3 --to update details of employee")
print(" 4 --to retrive particular employee")
print(" 5 --to delete details of employee")
print(" 6 --to exit")

class hospital:
    def getemployeedetails(self):
        self.employeeid=int(input("Enter emp id : "))
        self.name=input("Enter Name : ")
        self.phone=int(input("Enter phone number : "))
        self.div=input("Enter Employee Division : ")
        self.age=int(input("Enter Age of Employee "))
        self.experience=int(input("Enter the Employee experience: "))
        
    def printemployeedetails(self):
        print(f"Employee id : {self.employeeid}")
        print(f"Name of the employee : {self.name}")
        print(f"Employee Phone Number : {self.phone}")
        print(f"Designation of the employee : {self.div}")
        print(f"Age : {self.age}")
        print(f"experience of the employee : {self.experience}")

    def get_id(self):
        return self.employeeid

temp=[]
def find():
    for i in temp:
        i.printemployeedetails()
def retrive():
    for i in temp:
        i.printemployeedetails()
def delete(val):
    for i in temp:
        if(i.get_id()==value):
            temp.remove(i)

def modifyemployeedetails(value):
    print("---Employee---")
    print("1.Employeeid")
    print("2.Employee Name")
    print("3.PhoneNumber")
    print("4.Division")
    print("5.Age")
    print("6.Experience")
    n=int(input("enter your choice  to modify :"))
    for i in temp:
         if(i.get_id()==value):
            new=input("enter new value: ")
            if(n==1):
                i.employeeid=int(new)
            elif(n==2):
                i.name=new
            elif(n==3):
                i.phone=int(new)
            elif(n==4):
                i.div=new
            elif(n==5):
                i.age=new
            elif(n==6):
                i.experience=new
            else:
                break
for i in range(0,100):
    ch=int(input("Enter Your choice "))
    H1=hospital()
    if ch==1:
        H1.getemployeedetails()
        temp.append(H1)
    elif ch==2:
        retrive()
    elif ch==3:
        value=int(input("Enter employeeid to update"))
        modifyemployeedetails(value)
    elif ch==4:
        value=int(input("Enter the id to get find the employee details"))
        a=find()
    elif ch==5:
        value=int(input("Enter the id to delete"))
        delete(value)
    else:
        break
