"""
Number of students in class = M
number of quesstions in each paper = N
Number of courses = 5



ASSESSING STUDENTS IN CLASS
1. Receive index number of students into an array



MARKING OF PAPERS FOR A PARTICULAR COURSE:
1.  Receive examiner's anwers

2.  for each student:
i.      Create zero variable for student's mark - student_mark
ii.     Look through all student's answer and compare with examiner's answers
iii.    Every correct answer attracts an increment of one on student_mark
iv.     Append student_mark to  a subject_score array - course_marks
v.      Grade student_mark using a user-defined function according to the following
        70-100  A
        60-69   B
        50-59   C
        40-49   D
        0-39    F
vi.     Store grade in array for students grade - course_grades
END OF MARKING

After marking each paper for all students two will be three arrays,
all of which corresponds with the indices of the index number array
i. one containing students' mark and
ii. another containing students' grades

RANKING OF STUDENTS

1. Total all marks of each student for every course and store it in an array - subjects_total

2. Function to rank students from the highest to the lowest:
Function should receive subjects_total and return an array of arrays
i. e. A smaller array [student_index, student_rank] in a bigger one student_positions[]
Each smaller array contains a student's index number and his position in class

3. Fuction defined:
i.      Iterate through students marks and indices and store them as smaller list in a larger list
ii.     Rearrange student's list of index and total mark i.e sort smaller list in larger list in ascendence
iii.    Store the sorted list of lists in a variable say position_list
iv.     Give 1st position to 1st element of position_list
v.
END OF RANKING



"""

