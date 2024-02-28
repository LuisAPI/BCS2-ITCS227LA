# De La Salle University – Dasmariñas
# Luis Anton P. Imperial
# BCS22
# Monday, January 29, 2024

# Input: Name, Q1, Q2, Q3, P1, P2, P3, Assignment, Class Standing, Final Exam
# Do you want to enter new student record? Yes (1), No (2).
# Output: Grading System table.

from tabulate import tabulate

class GradingSystem_Imperial:
    def __init__(self):
        self.database = []

    def GetStudentOveralls(self, name: str, grade_q1: float, grade_q2: float, grade_q3: float,
                 grade_p1: float, grade_p2: float, grade_p3: float, grade_finalexam: float,
                 grade_asmt: float, grade_cstnd: float):
        self.name = name
        # Quizzes {1, 2, 3} grades
        self.grade_q1 = grade_q1
        self.grade_q2 = grade_q2
        self.grade_q3 = grade_q3
        # Projects {1, 2, 3} grades
        self.grade_p1 = grade_p1
        self.grade_p2 = grade_p2
        self.grade_p3 = grade_p3
        self.grade_finalexam = grade_finalexam
        # Class participation assignment grade
        self.grade_asmt = grade_asmt
        # Class standing grade
        self.grade_cstnd = grade_cstnd

        self.grade_qt = (self.grade_q1 + self.grade_q2 + self.grade_q3) / 3
        self.grade_pt = (self.grade_p1 + self.grade_p2 + self.grade_p3) / 3
        self.grade_ea = (self.grade_qt + self.grade_pt) / 2
        self.grade_cp = (self.grade_asmt + self.grade_cstnd) / 2
        self.grade_overall = (self.grade_ea * 0.5) + (self.grade_cp * 0.2) + (self.grade_finalexam * 0.3)
        if self.grade_overall >= 0.75:
            self.status = "Passed"
        else:
            self.status = "Failed"

        new_student = [self.name, self.grade_qt, self.grade_pt,
                       self.grade_asmt, self.grade_cstnd,
                       self.grade_finalexam, self.grade_overall, self.status]

        return new_student
    
    def AddToDatabase(self, new_student_input):
        self.database.append(new_student_input)

    def PrintDatabase(self):
        column_names = ["Name", "Quizzes", "Projects", "Assignment", "Standing", "Final Exam", "Grade", "Status"]
        print(tabulate(self.database, headers=column_names))

      
def main():
    print("Welcome to the University Grading System! Please input your first student's records.")
    inputting = True
    
    grade_sheet = GradingSystem_Imperial()

    while inputting:
        name = input("Name: ")
        grade_q1 = float(input("Quiz 1 Grade: "))
        grade_q2 = float(input("Quiz 2 Grade: "))
        grade_q3 = float(input("Quiz 3 Grade: "))
        grade_p1 = float(input("Project 1 Grade: "))
        grade_p2 = float(input("Project 2 Grade: "))
        grade_p3 = float(input("Project 3 Grade: "))
        grade_asmt = float(input("Assignments Grade: "))
        grade_cstnd = float(input("Class Standing Grade: "))
        grade_finalexam = float(input("Final Exam Grade: "))

        new_student_for_input = grade_sheet.GetStudentOveralls(
            name, grade_q1, grade_q2, grade_q3,
            grade_p1, grade_p2, grade_p3, grade_finalexam,
            grade_asmt, grade_cstnd
        )

        grade_sheet.AddToDatabase(new_student_for_input)
    
        inputting_response = input("\nDo you wish to enter another student's record? (y/n): ")
        if inputting_response == "y":
            inputting = True
            print("\nOK. Enter your next student's details:")
        else:
            inputting = False
            print("OK. Now printing the database table.\n")
    
    grade_sheet.PrintDatabase()

if __name__ == "__main__":
    main()