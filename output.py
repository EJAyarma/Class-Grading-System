def print_results_short(student_data):
    print_headers = True
    for student in student_data:
        # Print Headers Once
        if print_headers:
            for key in student.keys():
                print(key.upper(), end="\t\t\t")
            print()
            print_headers = False

        # Print student data
        for key in student.keys():
            print(student[key], end="\t\t\t")
        print()

def write_results_to_csv(student_data_list, filename, fiednames=["index_number", "total_mark", "position"]):
    with open(filename, 'w', newline="") as student_data_file:
        writer = csv.DictWriter(student_data_file, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_data_list:
            writer.writerow(student)