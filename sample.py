
class Employee(object):
    pass
    raise_amount=1.06
    num_of_employee=0
    def __init__(self, first, last, pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        # self.email=first + "." + last + "@company.com"
        Employee.num_of_employee+=1
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.fname,self.lname)
    @property
    def full_name(self):
        return "{} {}".format(self.fname, self.lname)
    @full_name.setter
    def full_name(self,obj):
        self.fname, self.lname=obj.split(" ")
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)
        return self.pay
    @classmethod
    def form_string(cls, emp_str):
        cls.fname,cls.lname,cls.pay= emp_str.split("-")
        return cls(cls.fname,cls.lname,cls.pay)
    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
    # def __str__(self):
    #     return "'{}' '{}' {}".format(self.fname,self.lname,self.pay)
    def __repr__(self):
        return "'{}' '{}' {}".format(self.fname,self.lname,self.pay)

emp1=Employee("Tarique","Siddique",6000)
emp1.full_name="Ashraf Siddique"
print emp1.full_name
