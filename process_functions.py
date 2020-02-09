"""Tunctions used to process students' data"""

from collections import OrderedDict

# Function for grade_student
def grade_student(mark):
    if (mark >= 70 and mark <= 100):
        return "A"
    elif (mark >= 60 and mark <= 69):
        return "B"
    elif (mark >= 50 and mark <= 59):
        return "C"
    elif (mark >= 40 and mark <= 49):
        return "D"
    elif (mark >= 0 and mark < 40):
        return "F"
    else:
        return ""
# end of grade_student()


# Define function to rank students
def rank_students(index_numbers, total_mark_all):
    index_rank_all = []
    student = OrderedDict(index_number=index_numbers[i], total_mark=total_mark_all[i], position="")
    for i in range(len(index_numbers)):
        index_rank_all.append(student)

    # Sort student data acoording to total mark
    index_rank_all.sort(key=lambda student_data: student_data["total_mark"])

    # Perform positioning
    for i, student_data in enumerate(index_rank_all, start=1):
        if i != 1:
            current_student = index_rank_all[i-1]
            previous_student = index_rank_all[i-2]
            if current_student["total_mark"] == previous_student["total_mark"]:
                current_student["position"] = previous_student["position"]
            else:
                student_data["position"] = i
        else:
            student_data["position"] = i
    
    return index_rank_all
    # end of rank_students()

