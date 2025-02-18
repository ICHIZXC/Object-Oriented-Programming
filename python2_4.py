import json

def main(value_in):
    try:
        first, sec, third, four = value_in.split('|')
        output_1 = add_score(json.loads(str(first).replace("'",'"')), sec.strip()[1:-1], third.strip()[1:-1].strip(), int(four))
        output_2 = calc_average_score(output_1) if output_1 != "Invalid" else "Invalid"
    
    except (ValueError, json.JSONDecodeError):
        return "Invalid"
    
    if output_1 == "Invalid" or output_2 == "Invalid":
        return "Invalid"
    
    return f"{output_1}, Average score: {output_2}"

def add_score(subject_score, student, subject, score):
    if not student or not isinstance(student, str):
        return "Invalid"
    if not subject or not isinstance(subject, str):
        return "Invalid"
    if not isinstance(score, int) or score < 0:
        return "Invalid"

    dict = subject_score.copy()

    if student in dict:
        dict[student][subject] = score
    else:
        dict[student] = {subject: score}
    
    return dict

def calc_average_score(dict):
    if not dict or len(dict) == 0:
        return "Invalid"

    sum_score = {}
    for student, subjects in dict.items():
        score_list = [
            score for score in subjects.values() 
            if isinstance(score, (int, float)) and score >= 0
        ]

        if not score_list:
            sum_score[student] = "0.00"
            continue
        
        average_score = sum(score_list) / len(score_list)
        sum_score[student] = "{:.2f}".format(average_score)
    
    return sum_score

x = input()
output = main(x)
print(output)