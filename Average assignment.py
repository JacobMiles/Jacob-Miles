Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information
>>> #Jacob Miles
def start():
    grade_1 = input("Grade in class 1: ")
    grade_2 = input("Grade in class 2: ")
    grade_3 = input("Grade in class 3: ")
    grade_4 = input("Grade in class 4: ")
    grade_5 = input("Grade in class 5: ")
    
    all_grades = [grade_1, grade_2, grade_3, grade_4, grade_5]
    average_grade = (int(grade_1) + int(grade_2) + int(grade_3) + int(grade_4) + int(grade_5)) / 5
    ag = "Average: " + str(average_grade)
    all_grades.append(ag)
    
    if average_grade < 60:
        print "Your average grade is a U."
    if average_grade >=  60 and average_grade < 70:
        print "Your average grade is a D."
    if average_grade >= 70 and average_grade < 80:
        print "Your average grade is a C."
    if average_grade >= 80 and average_grade < 90:
        print "Your average grade is a B."
    if average_grade >= 90:
        print "Your average grade is an A."
    print all_grades
    
    restart = input("Do you want to put in another set of grades?: ")
    if restart == "yes":
        start()
start()
