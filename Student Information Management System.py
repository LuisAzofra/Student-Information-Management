class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.enrollments = []  # List to store the course and the grade

    def enroll(self, course):
        self.enrollments.append((course, None)) 
    def record_grade(self, course_name, grade):
        for i, (course, _) in enumerate(self.enrollments):
            if course.name == course_name:
                self.enrollments[i] = (course, grade)
                return True
        return False

    def get_average_grade(self):
        total_grades = 0
        count = 0
        for _, grade in self.enrollments:
            if grade is not None:
                total_grades += grade
                count += 1
        return total_grades / count if count > 0 else 0
    def get_total_credit_hours(self):
        return sum(course.credit_hours for course, grade in self.enrollments if grade is not None)
class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
    def add_student(self, name, age, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age, student_id)
            print(f"Student {name} added successfully.")
        else:
            print(f"Student ID {student_id} already exists.")

    def add_course(self, name, credit_hours):
        if name not in self.courses:
            self.courses[name] = Course(name, credit_hours)
            print(f"Course {name} added successfully.")
        else:
            print(f"Course {name}already exists.")
    def enroll_student_in_course(self, student_id, course_name):
        if student_id in self.students and course_name in self.courses:
            student = self.students[student_id]
            course = self.courses[course_name]
            student.enroll(course)
            print(f"Student {student.name}  enrolled in {course.name}successfully.")
        else:
            print("Student ID or Course name is not valid.")

    def record_grade(self, student_id, course_name, grade):
        if student_id in self.students:
            student = self.students[student_id]
            if student.record_grade(course_name, grade):
                print(f"Grade {grade} recorded for {student.name} in {course_name}.")
            else:
                print(f"Student {student.name} is not enrolled in  {course_name}.")
        else:
            print(f"Student ID {student_id} not found.")

    def query_student_grades(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Grades for {student.name}:")
            for course, grade in student.enrollments:
                grade_display = grade if grade is not None else "Not graded"
                print(f"- {course.name}: {grade_display}")
        else:
            print(f"Student ID {student_id} not found.")
    def query_student_average_and_credits(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            avg_grade = student.get_average_grade()
            total_credits = student.get_total_credit_hours()
            print(f"Student: {student.name}")
            print(f"  Average Grade: {avg_grade:.2f}")
            print(f"Total Credit Hours: {total_credits}")
        else:
            print(f"Student ID {student_id}not found.")

    def query_course_info(self, course_name):
        if course_name in self.courses:
            course = self.courses[course_name]
            print(f"Course: {course.name}")
            print(f"  Credit Hours: {course.credit_hours}")
        else:
            print(f" Course {course_name} not found.")
if __name__ == "__main__":
    system = StudentManagementSystem()
    # Add students and courses
    system.add_student("Maria", 20,"S001")
    system.add_student("Luis", 22, "S002")
    system.add_course("Mathematics", 3)
    system.add_course("Physics", 4)
    system.add_course("Biology", 5)
    # Enroll students
    system.enroll_student_in_course("S001", "Mathematics")
    system.enroll_student_in_course("S002", "Physics")
    system.enroll_student_in_course("S001", "Biology")

    #Recording grades
    system.record_grade("S001", "Mathematics", 9.75)
    system.record_grade("S002", "Physics", 9)
    system.record_grade("S001", "Biology", 8.25)

    # grades and course information
    system.query_student_grades("S001")
    system.query_student_average_and_credits("S001")
    system.query_course_info("Mathematics")
