# What is Instance Variable and Class Variable.

class Employee:
    no_of_leaves = 8  # Yeh Class Variable hai - Yeh wali property (instance variable) DONO OBJECTS " SHARE " Karaigai
#  yeh no_of_leaves vaibhav ki nhi hai, rohan ki nhi hai, yeh dono share kar rhai hai, yeh iss class ki hai
#  kyunki dono vaibhav and rohan iss class sai derived hai (iss class kai objects hai) isliyai jo bhi instance variable class kai andar banaya jaiga wo yeh dono objects share karaigai,matlb yeh inn dono pai apply hoga, yeh inn dono ka hoga
# jitnai bhi app objects bnai gai iss class kai - yeh no_of_leaves sab kai liyai same hogi and sab ki hogi.

vaibhav = Employee()
rohan = Employee()

vaibhav.name = "Vaibhav Sharma"
vaibhav.salary = 500
vaibhav.role = "Web Developer"

rohan.name = "Rohan Gupta"
rohan.salary = 600
rohan.role = "App Developer"

print(rohan.name)
print(vaibhav.salary)

# name,salary,role are instance variable.
# no_of_leaves is a class variable.

# vaibhav ki salary hai jo wo vaibhav ki property hai
# rohan ka role hai jo wo rohan ki property hai
# name, salary, role iss object ki apni property hai, iss object ki apnai variable hai.
# inn varibles ka iss class (Employee) sai koi matlb nhi hai, yeh variable (name,salary,role) iss class sai nhi milai hai.

# agar esa variable chaiye jo class (Template) mai already maujuud jo, so how to do this
# How to access class variable
print(vaibhav.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
# above three lines same output.

# Now how to change the no_of_leaves
# How to change class variable
# As no_of_leaves is in class, so
# Can be CHANGED ONLY with CLASS NAME
Employee.no_of_leaves = 10
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(rohan.__dict__) # .__dict__ is a attribute, which returns the dictionary.

# Class Variable Can't be changed with the help of object.
rohan.no_of_leaves = 12  # this will create the new instance variable of the object rohan. rohan ki apni no_of_leaves change hui hai sirf, na ki sabhi employee's ki no_of_leaves change hui hai.
print(rohan.__dict__)
print(Employee.no_of_leaves)
print(Employee.__dict__)

# Class ki property sirf khud class hi change kar sakta hai
# rohan.no_of_leaves = 12 --> iss-sai sirf rohan object ki no_of_leaves wali property change hui, matlb no_of_leaves wali property sirf rohan object ki khud kai liyai change hui hai,
# esa nhi hua ki esa karnai sai sab kai liyai no_of_leaves wali property change ho gyi ho.
