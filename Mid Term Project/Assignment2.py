students_data = [("ali", "akber", "85", "55", "100"),
                 ("ahmed", "kamran", "55", "65", "95"),
                 ("waqas", "ali", "65", "45", "99"),
                 ("fawaz", "saim", "45", "65", "90"),
                 ("wasi", "saud", "75", "65", "90"),
                 ("fayaz", "farhan", "45", "55", "100"),
                ]
total_marks = 300
passing_marks = 50
for data in students_data:
    name = data[0]
    fname = data[1]
    maths_marks = int(data[2])
    physics_marks = int(data[3])
    sindhi_marks = int(data[4])
    total_marks_obtained = sum([maths_marks, physics_marks, sindhi_marks])
    percentage = (total_marks_obtained / total_marks) * 100
    if maths_marks >= passing_marks and physics_marks >= passing_marks and sindhi_marks >= passing_marks:
        result = "Passed"
    else:
        result = "Failed"
    print(name, "son of", fname, "has", result, "with total numbers", total_marks_obtained)
    print(name, "has scored percentage =", percentage)
    if total_marks_obtained > 200:
        result = "Promoted"
    else:
        result = "Demoted"
    print(name, "son of", fname, "is", result, "as this student obtained", total_marks_obtained)           