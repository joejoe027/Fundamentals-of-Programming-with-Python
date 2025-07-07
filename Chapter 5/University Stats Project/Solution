import random 

# This function randomizes the students that are enrolled in each class and their grades
def randomizeCourseEnrollment():
    courses = {
    "Math": [],
    "Science": [],
    "English": [],
    "Gym": []
    }
    
    student_names = ["Alex", "Tim", "Freddy", "John", "Mark", "Anne", "Julia", "Joe", "Sam", "Sarah", "Bob"]

    for course in courses:
        number_of_students = random.randint(3,7)  # Number of students to enroll
        selected_students = random.sample(student_names, number_of_students)  # No duplicates
    
        for student in selected_students:
            random_grade = random.randint(50, 101)
            courses[course].append((student, random_grade))
    
    return courses

courses = randomizeCourseEnrollment()

print("------------------------------------------")
print(f"This semester, course enrollment looked like this: {courses}")
print("------------------------------------------")

# Find The Class Average for each course
print("------------------------------------------")
for course in courses:
    sum = 0
    students = courses[course]
    for student in students:
        sum += student[1]
    print(f"The class average for {course} this semester was {sum/len(students)}%")
print("------------------------------------------")

# Find average for each student
students_averages = {}

print("------------------------------------------")
for course in courses:
    students = courses[course]
    for student,grade in students:
        if student not in students_averages:
            students_averages[student] = [grade,1]
        else:
            students_averages[student][0] += grade
            students_averages[student][1] += 1

for student in students_averages:
    total, count = students_averages[student]
    print(f"{student}'s average this semester was {total/count}%")
print("------------------------------------------")

# Find all students who were in Math and Gym Class
print("------------------------------------------")
math_students = set([student[0] for student in courses["Math"]])
gym_students = set([student[0] for student in courses["Gym"]])

math_and_gym_students = math_students.intersection(gym_students)
print(f"The students who completed math and gym are {math_and_gym_students}")
print("------------------------------------------")

# Find all the students who were in Gym but not English class
print("------------------------------------------")
gym_students = set([student[0] for student in courses["Gym"]])

english_students = set([student[0] for student in courses["English"]])

gym_but_not_english_students = gym_students.difference(english_students)

print(f"The students who were enrolled in gym but not english are {gym_but_not_english_students}")
print("------------------------------------------")


