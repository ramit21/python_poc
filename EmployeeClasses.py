class Employee: #by default inherits object class
    __id = None       #private variables with default values
    __name = ""
    __type = "Staff"
    __salary = 0
       
    #Constructor; self is like a this in Java
    def __init__(self, id, name, type, salary):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__salary = salary
    
    #Setter and getters for private variables
    def set_id(self, id) :
        self.__id = id
        
    def get_id(self):
        return self.__id
    
    def set_name(self, name) :
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_type(self, type) :
        self.__type = type
        
    def get_type(self):
        return self.__type
    
    def set_salary(self, salary) :
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
   
   #Public method; private methods would start with __, eg. __privateMethod()     
    def toString(self):
        return "Employee: id = {}, name = {}, type = {} and salary = {}".format(self.__id,
                                                                      self.__name,
                                                                      self.__type,
                                                                      self.__salary)
    #Method overloading
    def appraisal(self, hike=None)  :
        if hike is None:
            print('No appraisal this year')
        else:
            print('Salary hike is {}%'.format(hike))
            
    #Override equals and hashcode
    def __hash__(self):
        return hash((self.__id, self.__name))

    def __eq__(self, other):
        return (self.__id, self.__name) == (other.__id, other.__name)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)  



          
            
#Inheritance        
class Manager(Employee):
    __grade = ""
    
    def __init__(self, id, name, type, salary, grade):
        self.__grade = grade
        super(Manager, self).__init__(id, name, type, salary)
        
    def set_grade(self, grade) :
        self.__grade = grade
        
    def get_grade(self):
        return self.__grade
    
    #Method overriding
    def toString(self):
        return "Manager: id = {}, name = {}, type = {}, salary = {} and grade = {}".format(self.get_id(),
                                                                      self.get_name(),
                                                                      self.get_type(),
                                                                      self.get_salary(),
                                                                      self.__grade)  
    
    
    