def most_money(students):

    def count_money(student):
        return 5 * student.fives + 10 * student.tens + 20 * student.twenties

    counted_money = sorted(tuple((student.name, count_money(student)) for student in students), key=lambda x: x[1], reverse=True)
    print(counted_money)
    if len(students) > 1 and counted_money[0][1] == counted_money[1][1]:
        return "all"
    else:
        return counted_money[0][0]
