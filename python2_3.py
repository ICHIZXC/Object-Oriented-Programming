import json

def add_score(sub_score, sub, score):

    score = int(score)
    sub = sub.strip("'")
    
    if sub == '' or score < 0:
        return '{}'
    
    sub_score[sub] = score
    
    return sub_score

def calc_avg_score(sub_score):
    total = sum(sub_score.values())
    avg = total / len(sub_score) if sub_score else 0
    return round(avg, 2)

subject_score, sub, score = input().split(' | ')
sub_score = json.loads(subject_score.replace('\'', '\"'))

print(f"{add_score(sub_score, sub, score)}, Average score: {calc_avg_score(sub_score):.2f}")