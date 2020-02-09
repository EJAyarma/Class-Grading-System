"""This module is the main program coordinating the class grading system"""

from process_functions import grade_student, rank_students
from output import print_results_short

students_num = int(input("Enter the number of students\n"))
index_numbers = []
total_mark_all = [0 for i in range(students_num)]
print("Provide the index number of studens\n")
for i in range(students_num):
    print("Number of students left: {}".format(students_num - i))
    student_index = input("\n")
    index_numbers.append(student_index)


course_names = []
course_marks_all = []
course_grades_all = []

courses_num = int(input("Enter the number of courses\n"))

# Marking papers for a particular course
print("Please get ready to mark papers\n")
for course in range(courses_num):
    course_marks = []
    coursename = input("Enter name of course\n")
    course_grades = []
    questions_num = int(input("Enter the number of questions in a paper\n"))

    # Receive examiner's answers, compare with that of students for scoring

    ans_examiner = [] 
    print("Enter Examiner's answers")
    for q in range(questions_num):
        print("Question {}".format(q + 1))  
        ans = input("\n")
        while (int(ans) < 1 or int(ans) > 5):  
            print("Answer must be in the range 1 - 5\n")
            ans = input("\n")
        ans_examiner.append(ans)  

    for index_num in range(len(index_numbers)):  
        ans_student = []
        track_message = "Enter answers for student with index number "
        track_message += index_numbers[index_num]
        print(track_message)
        for m in range(questions_num):
            print("Question {}".format(m + 1))  
            ans = input("\n")
            while (int(ans) < 1 or int(ans) > 5):  
                print("Answer must be in the range 1 - 5\n")
                ans = input("\n")
            ans_student.append(ans)  

        # Mark student's paper
        student_mark = 0
        for i in range(len(ans_student)):
            if (ans_student[i] == ans_examiner[i]):
                student_mark += 1
        total_mark_all[index_num] += student_mark
        
        # Update student's data
        course_marks.append(student_mark)  
        student_grade = grade_student(student_mark)
        course_grades.append(student_grade)

    # Update course data for class
    course_names.append(coursename)
    course_marks_all.append(course_marks)
    course_grades_all.append(course_grades)

# Rank students
student_data = rank_students(index_numbers, total_mark_all)
print_results_short(student_data)