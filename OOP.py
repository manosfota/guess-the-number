class Employee():
  def __init__(self,first,last,pay):
    self.first=first
    self.last=last
    self.pay=pay
    self.email=first + '.' + last + '@gmail.com'

empl_1=Employee()
empl_2=Employee()


empl_1.first='Corey'
empl_1.last='Jones'
empl_1.email='lonecor@gmai.com'
empl_1.pay=2000

empl_2.first='Tom'
empl_2.last='Paul'
empl_2.email='paultom@gmai.com'
empl_2.pay=2000

print(empl_1.email)



