from src.School import School
from src.Student import Student

from random import SystemRandom

from src.School import School
from src.Student import Student


def main():
    school = School("14-High School")

    # school.add_student(Student(1, "John Mark", "8th grade"))
    # school.add_student(Student(2, "Jack Mark", "9th grade"))
    # school.add_student(Student(3, "John Doe", "10th grade"))
    # school.add_student(Student(4, "Charlie Brown", "12th grade"))
    #
    # school.delete_student(5)

    while True:
        print("\n1. Add student")
        print("2. Delete student")
        print("3. Mark Attendance")
        print("4 Show Attendance")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            student_id = school.get_number_of_students() + 1
            full_name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            school.add_student(Student(student_id, full_name, grade))
        elif choice == '2':
            school.show_students_details()
            student_id = int(input("Enter student id to delete: "))
            school.delete_student(student_id)
        elif choice == '3':
            school.mark_attendance()
        elif choice == '4':
            school.show_attendance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()