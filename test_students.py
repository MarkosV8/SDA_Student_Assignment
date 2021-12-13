import pytest
from students import Students

def test_body_mass_index():
    assert Students(weight = 80, height = 180).body_mass_index() 
    assert Students(weight = 78, height = 150).body_mass_index()
    assert Students(weight = 42, height = 210).body_mass_index()
    assert Students(weight = 30, height = 150).body_mass_index()

def test_ideal_weight():
    assert Students(gender="male", height= 160, age = 50).ideal_weight()
    assert Students(gender="female", height= 130, age = 15).ideal_weight()
    assert Students(gender="male", height= 300, age = 80).ideal_weight()
    assert Students(gender="female", height= 211, age = 53).ideal_weight()  

def test_days_alive():
    assert Students(age=30).days_alive()
    assert Students(age=11).days_alive()
    assert Students(age=22).days_alive()
    assert Students(age=15).days_alive()

def test_grade_to_list():
    test1 = Students()
    test1.grade_to_list("Test1", "5")
    test1.grade_to_list("Test2", "2")
    assert test1.grades["Test2"]
    test2 = Students()
    test2.grade_to_list("Test3", "1")
    test2.grade_to_list("Test4", "5")
    assert test2.grades["Test3"]

def  test_calc_average_grade():
    test3 = Students()
    test3.grade_to_list("Test5", "5")
    test3.grade_to_list("Test6", "4")
    test3.grade_to_list("Test7", "3")
    test3.grade_to_list("Test8", "2")
    test3.grade_to_list("Test9", "1")
    test3.grade_to_list("Test10", "5")
    assert test3.calc_average_grade()