class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Ism: {self.name}")
        print(f"Yosh: {self.age}")


class UniversityStudent(Student):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty

    def display_info(self):
        super().display_info()
        print(f"Faculty: {self.faculty}")


class GraduateStudent(UniversityStudent):
    def __init__(self, name, age, faculty, thesis_topic):
        super().__init__(name, age, faculty)
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for i, student in enumerate(self.students):
            print(f"Student {i+1}:")
            student.display_info()
            print("-------------------")


student_management_system = StudentManagementSystem()
student1 = Student("Ali", 20)
student2 = UniversityStudent("Vali", 22, "Mathematics")
student3 = GraduateStudent("Salim", 24, "Physics", "Quantum Mechanics")
student_management_system.add_student(student1)
student_management_system.add_student(student2)
student_management_system.add_student(student3)
student_management_system.display_all_students()