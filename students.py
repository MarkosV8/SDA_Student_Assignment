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
        self.grades.append({course:grade})
        return self.grades

    #Function to calculate Students average grades
    def calc_average_grade(self):
        number_of_grades = 0
        sum_of_grades = 0
        for number, value in self.grades.items():
            number_of_grades += 1
            sum_of_grades += int(value)
        return (sum_of_grades / number_of_grades)


elvis = Students(19, 67, 178, "Elvis", "Robinson",  "male")
andre = Students(21, 80, 163, "Andre", "Jobs", "male")
grey = Students(23, 60, 155, "Grey", "Almond", "female")
maria = Students(30, 80, 173, "Maria", "Tremble", "female")

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
print("")

