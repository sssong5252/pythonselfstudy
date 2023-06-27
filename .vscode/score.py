def grade_to_score(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0
    elif grade == 'P':
        return None


def major_score(subjects):
    total_credit = total_score = 0
    for name, credit, grade in subjects:
        credit = float(credit)
        score = grade_to_score(grade)
        
        if score is None:
            continue
        
        total_credit += credit
        total_score += credit * score
    
    return total_score / total_credit


def input_subject():
    subject = input().split()
    return (subject[0], subject[1], subject[2])


def main():
    subjects = [input_subject() for _ in range(20)]

    print(format(major_score(subjects), ".6f"))


if __name__ == "__main__":
    main()
