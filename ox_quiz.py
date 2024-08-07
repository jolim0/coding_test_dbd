def solution(quiz):
    res = []
    for q in quiz:
        X, operatopr, Y, _, Z = q.split(" ")

        X = int(X)
        Y = int(Y)
        Z = int(Z)

        if operatopr == "+":
            if X + Y == Z:
                res.append("O")
            else:
                res.append("X")

        if operatopr == "-":
            if X - Y == Z:
                res.append("O")
            else:
                res.append("X")

    return res


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
