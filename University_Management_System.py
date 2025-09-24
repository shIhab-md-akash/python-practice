# Module 7 Assignment - University Management System


class Person:
    total_people = 0   # class variable to count all persons

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."

    @classmethod
    def get_total_people(cls):
        return cls.total_people



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = 0.0   
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    def enroll_course(self, course):
        self.course_list.append(course)

    def show_courses(self):
        return self.course_list

   
    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("S-")



class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    
    def introduce(self):
        return f"I am Professor {self.name}, teaching {self.subject}."



def display_role(person):
    if isinstance(person, Student):
        return f"{person.name} is a Student."
    elif isinstance(person, Teacher):
        return f"{person.name} is a Teacher."
    else:
        return "Unknown role."



class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title



if _name_ == "_main_":
    # Create Student
    s1 = Student("Alice", 20, "S-101")
    s1.gpa = 3.8
    s1.enroll_course("Math")
    s1.enroll_course("CS")
    print(s1.introduce())
    print("Courses:", s1.show_courses())
    print("GPA:", s1.gpa)

    
    t1 = Teacher("Dr. Smith", 405, "T-201", "Physics")
    print(t1.introduce())

    
    g1 = GraduateStudent("Bob", 24, "S-202", "AI in Healthcare")
    print(g1.introduce(), "Thesis:", g1.thesis_title)

    # Polymorphism
    print(display_role(s1))
    print(display_role(t1))

    # Class Method
    print("Total People:", Person.get_total_people())

    # Static Method Check
    print("Valid ID?", Student.is_valid_id("S-999"))
    print("Valid ID?", Student.is_valid_id("X-123"))
