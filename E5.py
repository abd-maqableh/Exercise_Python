class Employee:
    
    def __init__(self,emNo,Name,Address,Salary,JobTitle):
        
        self.emNo=emNo
        self.__Name=Name
        self.__Address=Address
        self.__Salary=Salary
        self.__JobTitle=JobTitle
        
    def getName(self):
        
        return self.__Name
    def getAddress(self):
        
        return self.__Address
    def setAddress (self,address):
        
        self.__Address = address
    def getSalary (self):
        return self.__Salary
    
    def getJobTitle (self):
        return self.__JobTitle
    
   
        
    def info1 (self):
        print( " Employee number:", self.emNo)
        print( " Name:", self.getName()) 
        print( " Address:", self.getAddress()) 
        print( " Salary:", self.getSalary())
        print( " Job Title:", self.getJobTitle())
        
        
    def info2 (self):
        print( " Employee number:", self.emNo , end = ",")
        print( " Name:", self.getName(), end = ",") 
        print( " Address:", self.getAddress(), end = ",") 
        print( " Salary:", self.getSalary(), end = ",")
        print( " Job Title:", self.getJobTitle(), end = ",")   
     
    def __del__(self):
        
        print(self.__Name + " has been deleted")    
        

E1 = Employee(1,"Mohammad Khalid","Amman,Jordan",500,"Consultant")

E2 = Employee(2,"Hala Rana","Aqaba,Jordan",750,"Manager")    

E1.info1() 
E2.info2()

E1.setAddress("USA")


print("Employee1 New Address : ", end ="")
print(E1.getAddress())


print("\n")

del E1
del E2
