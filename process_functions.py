"""This module contains functions we'll use to process students' data"""

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
def rank_students(index_numbers, mark_list):
    mark_list_temp = mark_list[:]
    index_rank_all = []
    index_rank_all_processed = []  # Position list
    # iterate through students marks and indices and store them as lists in a list
    for i in index_numbers:
        index_rank = []
        index_rank.append(i)
        index_rank.append(mark_list_temp[index_numbers.index(i)])
        index_rank_all.append(index_rank)
    # Rearrange student's list of index and total mark
    for i in index_numbers:
        highest_mark = max(mark_list_temp)  # index of highest mark
        index_rank_all_processed.append(index_rank_all[mark_list_temp.index(highest_mark)])  # Add to position list
        index_rank_all.remove(
            index_rank_all[mark_list_temp.index(highest_mark)])  # remove instance of list of highest mark
        mark_list_temp.remove(highest_mark)  # remove instance of highest mark
    # Perform positioning
    index_rank_all_processed[0].append(1)  # Give 1st position to 1st element of position list
    # Continue
    position_count = 2
    for i in range(1, len(index_rank_all_processed), 1):
        if (index_rank_all_processed[i - 1][1] == index_rank_all_processed[i][
            1]):  # Does total mark in position list occur more than once?
            index_rank_all_processed[i].append(index_rank_all_processed[i - 1][-1])  # Then they'll have same position
            position_count += 1
        else:
            index_rank_all_processed[i].append(position_count)  # Otherwise one person takes position
            position_count += 1
    return index_rank_all_processed  # lists in list in the form of smaller_list[index_number, total_mark, position]
# end of rank_students()

