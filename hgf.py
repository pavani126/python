class Employee:
  def __init__(self,eno,esal):
    self.empno=eno
    self.empsal=esal
  def setempage(self,eage):
    while eage<21 or eage>58:
      eage=int(input("pls enter age between 21 to 58:"))
    self.empage=eage
  def getempage(self):
    return self.empage
  def displayempInfo(self):
    print("employee number is:",self.empno)
    print("employee salary is:",self.empsal)
obj=Employee(111,1000)
obj.displayempInfo()
age=int(input("enter empage is:"))
obj.setempage(age)
print("empage is:",obj.getempage())
     
      
    