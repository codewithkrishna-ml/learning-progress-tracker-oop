#PROJECT-Learning-Progress-Tracker
import re
import csv
import json

class Course:
    def __init__(self, course_name, required_points):
        self.course_name = course_name
        self.required_points = int(required_points)

    def __str__(self):
        return f"'{self.course_name}' (Required Points: {self.required_points})"

class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolled_courses = {'Python': 0, 'Java': 0, 'Data Science': 0}

    def add_points(self, course_name, points):
        if points > 0:
            if course_name in self.enrolled_courses:
                self.enrolled_courses[course_name] += points
                return True
            else:
                print(f"Error: Course named '{course_name}' does not exist.")
                return False
        else:
            print("Error: Points must always be greater than 0!")
            return False

    def get_progress(self, course_name, required_points):
        current_points = self.enrolled_courses.get(course_name, 0)
        if required_points == 0:
            return 0.0
        percentage = (current_points / required_points) * 100
        return min(percentage, 100.0)

class TrackerSystem:
    def __init__(self):
        self.students = {}
        self.courses = {
            'Python': Course('Python', 600),
            'Java': Course('Java', 500),
            'Data Science': Course('Data Science', 400)
        }
        self.current_id = 10001

    def add_student(self, first_name, last_name, email):
        if not first_name.strip() or not last_name.strip():
            print("Error: First name and last name cannot be empty.")
            return False

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Error: Invalid email format.")
            return False

        for student in self.students.values():
            if student.email == email:
                print("Error: This email is already registered.")
                return False

        new_student = Student(self.current_id, first_name, last_name, email)
        self.students[self.current_id] = new_student
        print(f"Student {first_name} {last_name} successfully added! ID: {self.current_id}")
        self.current_id += 1
        return True

    def find_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        else:
            return None

    def add_points_to_student(self, student_id, python_pts, java_pts, ds_pts):
        student = self.find_student(student_id)
        if student is None:
            print(f"Error: Student with ID {student_id} not found.")
            return False

        student.add_points('Python', python_pts)
        student.add_points('Java', java_pts)
        student.add_points('Data Science', ds_pts)
        print(f"Points successfully updated for Student ID {student_id}")
        return True

    def show_stats(self):
        if not self.students:
            print("The system currently has no students registered.")
            return 

        print("\n------------ COURSE STATISTICS ---------------")
        for c_name, course_obj in self.courses.items():
            print(f"\nCourse: {course_obj.course_name}")
            for s_id, student in self.students.items():
                pts = student.enrolled_courses[c_name]
                prog = student.get_progress(c_name, course_obj.required_points)
                print(f"-> Student: {student.first_name} (ID: {s_id}) | Points: {pts} | Progress: {prog:.2f}%")

    def show_table_format(self):
        if not self.students:
            print("No student data available to display in table.")
            return

        print("\n" + "="*85)
        print(f"{'STUDENT ID':<12} | {'FULL NAME':<20} | {'PYTHON (600)':<14} | {'JAVA (500)':<14} | {'DS (400)':<12}")
        print("="*85)
        
        for s_id, s in self.students.items():
            py_p = f"{s.enrolled_courses['Python']} ({s.get_progress('Python', 600):.1f}%)"
            jv_p = f"{s.enrolled_courses['Java']} ({s.get_progress('Java', 500):.1f}%)"
            ds_p = f"{s.enrolled_courses['Data Science']} ({s.get_progress('Data Science', 400):.1f}%)"
            full_name = f"{s.first_name} {s.last_name}"
            print(f"{s_id:<12} | {full_name:<20} | {py_p:<14} | {jv_p:<14} | {ds_p:<12}")
        print("="*85)

    def export_to_csv(self, filename="learn_matrix_data.csv"):
        if not self.students:
            print("No records found to export to CSV.")
            return

        headers = ['StudentID', 'FirstName', 'LastName', 'Email', 'Python_Pts', 'Java_Pts', 'DataScience_Pts']
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for s in self.students.values():
                    writer.writerow([
                        s.student_id, s.first_name, s.last_name, s.email,
                        s.enrolled_courses['Python'], s.enrolled_courses['Java'], s.enrolled_courses['Data Science']
                    ])
            print(f"Success: Data successfully exported to Excel spreadsheet format: '{filename}'")
        except Exception as e:
            print(f"Failed to export CSV: {e}")

    def save_to_json(self, filename="learn_matrix_data.json"):
        if not self.students:
            print("No records found to save as JSON.")
            return

        data_to_save = {}
        for s_id, s in self.students.items():
            data_to_save[s_id] = {
                "first_name": s.first_name,
                "last_name": s.last_name,
                "email": s.email,
                "points": s.enrolled_courses
            }
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=4)
            print(f"Success: Data structural tree successfully saved as: '{filename}'")
        except Exception as e:
            print(f"Failed to save JSON: {e}")


system = TrackerSystem()

while True:
    print("\n------------ LEARN MATRIX MENU -----------------")
    print("1. Add Student")
    print("2. Find Student")
    print("3. Add Points")
    print("4. Standard Stats View")
    print("5. Display Beautiful Matrix Table")
    print("6. Export Student Progress Data to CSV")
    print("7. Save System Records as JSON File")
    print("8. Exit")

    choice = input("Select an option (1-8): ").strip()

    if choice == "1":
        f_name = input("Enter the First Name: ").strip()
        l_name = input("Enter the Last Name: ").strip()
        email = input("Enter Email: ").strip()
        system.add_student(f_name, l_name, email)

    elif choice == "2":
        try:
            s_id = int(input("Enter Student ID: ").strip())
            student = system.find_student(s_id)
            if student:
                print(f"\nStudent Details Found:")
                print(f"ID: {student.student_id} | Name: {student.first_name} {student.last_name} | Email: {student.email}")
                print(f"Points Matrix: {student.enrolled_courses}")
            else:
                print("Error: Student not found")
        except ValueError:
            print("Error: ID must always be a valid number!")

    elif choice == "3":
        try:
            s_id = int(input("Enter Student ID: ").strip())
            print("Enter points for each course (use 0 or a positive number):")
            p_pts = int(input("Python Points: ") or 0)
            j_pts = int(input("Java Points: ") or 0)
            d_pts = int(input("Data Science Points: ") or 0)
            system.add_points_to_student(s_id, p_pts, j_pts, d_pts)
        except ValueError:
            print("Error: Please input correct numerical values!")

    elif choice == "4":
        system.show_stats()
        
    elif choice == "5":
        system.show_table_format()
        
    elif choice == "6":
        system.export_to_csv()
        
    elif choice == "7":
        system.save_to_json()

    elif choice == "8":
        print("Thank you for using LearnMatrix! Goodbye.")
        break
    else:
        print("Invalid choice! Please select a number between 1 and 8.")

