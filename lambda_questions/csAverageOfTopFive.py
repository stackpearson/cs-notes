def csAverageOfTopFive(scores):
    # scores is a list of lists
    # each inner list has two elements: inner[0] = student id
    #                                   inner[1] = score
    # gather the top 5 scores for each student and average them
    # make a dict with student id as key and scores as the value
    students_to_scores = {} # key: student id, value is list of scores
    for elem in scores: 
        student_id = elem[0]
        score = elem[1]
        if student_id not in students_to_scores: 
            students_to_scores[student_id] = []
        student_scores = students_to_scores[student_id]
        student_scores.append(score)
    sorted_student_ids = sorted(students_to_scores.keys())
    top_five_averages = []
    print(sorted_student_ids)
    for student_id in sorted_student_ids: # O(n) where n is number of unique students
        sorted_scores = sorted(students_to_scores[student_id], reverse=True) # O(n log n) where n is num of scores for student
        top_five = sorted_scores[:5]
        print("top_five", top_five)
        average = sum(top_five) // len(top_five)
        top_five_averages.append([student_id, average])
    return top_five_averages