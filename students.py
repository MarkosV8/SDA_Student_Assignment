class Students:
    #Constructor
    def __init__(self, age = 0, weight = 0, height = 0, first_name = "first name", last_name = "last name", gender  = "male or female"):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
        self.gender = gender

    #Function to calculate Students body mass index
    def body_mass_index(self):
        body_mass_index = (self.weight/((self.height/100)**2))
        return round(body_mass_index, 2)

    #Function to calculate Students ideal weight
    def ideal_weight(self):
        if self.gender == "male":
            ideal_weight = int((3 * self.height - 450 + self.age)* 0.250 + 45.0)
        else:
            ideal_weight =  int((3 * self.height - 450 + self.age)* 0.225 + 40.5)
        return ideal_weight

    #Function to determine how many days students has been alive
    def days_alive(self):
        return self.age*365

    #Function to add Students grades to gradelist
    def grade_to_list(self, course, grade):
        self.grades.update({course:grade})
        return self.grades

    #Function to calculate Students average grades
    def calc_average_grade(self):
        number_of_grades = 0
        sum_of_grades = 0
        for number, value in self.grades.items():
            number_of_grades += 1
            sum_of_grades += int(value)
            return round(sum_of_grades / number_of_grades)

elvis = Students(19, 67, 178, "Elvis", "Robinson",  "male")
andre = Students(18, 80, 163, "Andre", "Jobs", "male")
grey = Students(20, 60, 155, "Grey", "Almond", "female")
maria = Students(17, 80, 173, "Maria", "Tremble", "female")

print("______________________________________________________________")
print(f"""By knowing how much every student weights:
Elvis: {elvis.weight}kg, Andre: {andre.weight}kg, Grey: {grey.weight}kg, Maria: {maria.weight}kg,
We can calculate their body mass indexes. 
Elvis: {elvis.body_mass_index()}, Andre: {andre.body_mass_index()}, Grey: {grey.body_mass_index()}, Maria: {maria.body_mass_index()}""")
print("______________________________________________________________")
print(f"""As of 2021 students are very determined about their weight. So with their weight,
we can also calculate their ideal weight
Elvis: {elvis.ideal_weight()}, Andre: {andre.ideal_weight()}, Grey: {grey.ideal_weight()}, Maria: {maria.ideal_weight()} """)
print("______________________________________________________________")
print(f"""Here is how many days Students have lived.
Elvis: {elvis.days_alive()}days, Andre: {andre.days_alive()}days, Grey: {grey.days_alive()}days, Maria: {maria.days_alive()}days""")
print("______________________________________________________________")
elvis =  Students()
elvis.grade_to_list("Math", "5")
elvis.grade_to_list("Russian", "2")
elvis.grade_to_list("Science", "3")
andre = Students()
andre.grade_to_list("Math", "2")
andre.grade_to_list("Russian", "2")
andre.grade_to_list("Science", "2")
grey = Students()
grey.grade_to_list("Math", "5")
grey.grade_to_list("Russian", "5")
grey.grade_to_list("Science", "5")
maria = Students()
maria.grade_to_list("Math", "4")
maria.grade_to_list("Russian", "2")
maria.grade_to_list("Science", "1")

for course, value in elvis.grades.items():
    print(f"Elvises {course} class has been graded as {value}")
print("______________________________________________________________")
for course, value in andre.grades.items():
    print(f"Andres {course} class has been graded as {value}")
print("______________________________________________________________")
for course, value in grey.grades.items():
    print(f"Greys {course} class has been graded as {value}")
print("______________________________________________________________")
for course, value in maria.grades.items():
    print(f"Marias {course} class has been graded as {value}")
print("______________________________________________________________")
print(f"""Elvises average course grade is {elvis.calc_average_grade()}
Andres average course grade is {andre.calc_average_grade()}
Greys average course grade is {grey.calc_average_grade()}
Marias average course grade is {maria.calc_average_grade()}""")
