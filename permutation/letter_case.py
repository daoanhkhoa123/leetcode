def letter_case(string):
    res = [""]

    for c in string:
        tmp = []
        if c.isalpha():
            for r in res:
                tmp.append(r + c.upper())
                tmp.append(r + c.lower())

        else:
            for i, r in enumerate(res):
                tmp.append(r + c)

        res = tmp

    return res



letter_case("a1b2c3")