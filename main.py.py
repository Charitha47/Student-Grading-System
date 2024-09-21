# Student Grade Management System

class GradeBook:

    # Constructor to call when the object is created
    def __init__(self):
        # Display a welcome message
        print("You have created a new grade Book")
        # Create an empty dictionary to where keys are student names and values are dictionaries with subjects & scores
        self.grade_book = dict()

    # Function to check if the student is present in the grade book
    def check_student(self, name):
        # Check if name is present in grade book and return accordingly
        return name in self.grade_book.keys()

    # Function to add a student into the grade book
    def add_student(self, name):
        # Check if the student is present
        if not self.check_student(name):
            # If student is not present, initialize a dictionary to hold subjects and scores for the student
            student_grades = dict()
            # Add the student to the grade book dictionary
            self.grade_book[name] = student_grades
        else:
            # Print message if student is already present
            print("Student is already present")

    # Function to calculate average of the student
    def calculate_student_average(self, name):
        # Check if the student is present in grade book
        if self.check_student(name):
            try:
                # Find total scores in all subjects and return average
                average = sum(self.grade_book[name].values()) / len(self.grade_book[name])
                return average
            except ZeroDivisionError:
                # Handle zero division error if no subjects are present for the current student
                print("Student is not enrolled in any subjects")

    # Function to display scores of a student in all subjects
    def view_student_grades(self, name):
        # Check if the student is present
        if self.check_student(name):
            print("Grades of {} are as follows".format(name))
            # Display subject and it's score for the current student
            for subject in self.grade_book[name]:
                print("Subject : {0} Score : {1}".format(subject, self.grade_book[name][subject]))
        else:
            # Error message if the student is not present
            print("Student is not present in the grade book")

    def remove_student_record(self, name):
        # Using try-except to handle exceptions
        try:
            # Try to remove student record from dictionary
            self.grade_book.pop(name)
            # Display success message
            print(name, " is removed from the records")
        except KeyError:
            # Throw error message if student is not present
            print("Student is not present in the grade book")


    # Function to update student record
    def update_student_grade(self, name, subject_name, new_grade):
        # Check if student name is present in grade book
        if not self.check_student(name):
            # If name is not present, add the student to the grade book
            self.add_student(name)
        # Update the student's grade record
        self.grade_book[name][subject_name] = new_grade

    # Function to display student's ranking
    def view_student_ranking(self):
        # Create a dictionary dor student's ranking
        student_ranking = dict()
        # Check if the grade book is empty
        if len(self.grade_book) == 0:
            print("Grade Book is empty")

        # Calculate and store averages of all students
        for student in self.grade_book:
            student_ranking[student] = self.calculate_student_average(student)

        # Sort the dictionary based on the average score of each student in descending order
        student_ranking = sorted(student_ranking.items(), key=lambda pair: pair[1], reverse=True)
        # Set starting rank to 1
        rank = 1
        # Display all student's rank and their average score
        for student, score in student_ranking:
            print("Rank:{0} Student:{1} Avg Score:{2}".format(rank, student, score))
            rank += 1

    # Function which return list of all available students
    def fetch_all_students(self):
        return list(self.grade_book.keys())

    # Function to calculate final letter grade of all students
    def calculate_final_letter_grade(self):
        # Fetch all students
        student_list = self.fetch_all_students()
        # Create a dictionary
        student_final_grade = dict()
        # Calculate letter grade of all students based on average score
        for student in student_list:
            student_final_grade[student] = self.calculate_letter_grade(self.calculate_student_average(student))
        # Return updated dictionary
        return student_final_grade

    # Function to display all student]'s final grade
    def view_student_final_grade(self):
        # Fetch the final letter grade of all students
        student_final_grade = self.calculate_final_letter_grade()
        if len(student_final_grade) == 0:
            print("Grade Book is empty")
            # Display all student's final grade
        for student in student_final_grade:
            print("Student:{0} Grade:{1}".format(student, student_final_grade[student]))

    @staticmethod
    # Function to check if user intends to insert another student record
    def request_additional_record():
        print("Do you want to insert student record?")
        user_input = input("Enter 0 for No or any natural number for Yes (Any key other than 0 is considered Yes)")
        # Return choice of user as boolean
        if user_input == "0":
            return False
        return True

    # Function to get details from user and update student record
    def update_current_record(self):
        # Get student name
        student_name = self.request_student_name()
        # Get subject name and scores
        subject, score = self.request_student_subject_details()
        # Update student's record
        self.update_student_grade(student_name, subject, score)

    # Function to check if user intends to add another record and update the same
    def update_student_record(self):
        # Request records until user inputs to stop key
        while self.request_additional_record():
            # Update current student record
            self.update_current_record()

    @staticmethod
    # Function to display user options and get user input
    def get_user_input():
        # Tuple for allowed user options
        user_options = ("a", "b", "c", "d", "e", "x")
        # Selection options
        print("Input key \"A\" to insert a student record")
        print("Input key \"B\" to view student's individual scores")
        print("Input key \"C\" to view all students final letter grade")
        print("Input key \"D\" to view all students ranking based on avg")
        print("Input key \"E\" to remove a student record")
        print("Input key \"X\" to exit the program")

        user_input = input("Enter your selection")

        # Ensure valid input is received from user
        while user_input.lower() not in user_options:
            print("Please input valid option")
            user_input = input("Enter your selection")
        # Return user input
        return user_input.lower()

    # Driver function for user interaction
    def main(self):
        user_input = self.get_user_input()
        # Do relevant function based on user input
        while user_input != "x":
            if user_input == "a":
                self.update_student_record()
                print("Student's record is updated")
            elif user_input == "b":
                name = self.request_student_name()
                self.view_student_grades(name)
            elif user_input == "c":
                self.view_student_final_grade()
            elif user_input == "d":
                self.view_student_ranking()
            elif user_input == "e":
                name = self.request_student_name()
                self.remove_student_record(name)
            user_input = self.get_user_input()
        print("Program ended successfully!")

    @staticmethod
    # Function to request name of the student
    def request_student_name():
        return input("Input the name of the student")

    @staticmethod
    # Function to request subject details
    def request_student_subject_details():
        # Request subject name
        subject_name = input("Input the name of the subject")
        while True:
            try:
                # Request subject score
                subject_score = int(input("Input the subject's score"))
                # Return subject details
                return subject_name, subject_score
            except ValueError:
                # Handle exception for invalid input
                print("Please input only integer values")

    @staticmethod
    # Function to calculate letter grade based on average score
    def calculate_letter_grade(score):
        # Letter grade is A for score greater than or equal to 90
        if score >= 90:
            return "A"
        # Letter grade is B for score greater than or equal to 80
        elif score >= 80:
            return "B"
        # Letter grade is C for score greater than or equal to 70
        elif score >= 70:
            return "C"
        # Letter grade is D for score greater than or equal to 60
        elif score >= 60:
            return "D"
        # Letter grade is F for score less than 60
        else:
            return "F"


# Initialize grade book object
gradeBook = GradeBook()
# Call the driver function
gradeBook.main()
