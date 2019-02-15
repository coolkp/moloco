def equalsWhenOneCharRemoved(x, y):
    if abs(len(x) -len(y)) != 1:
        return False
    i = 0
    j = 0
    skip = 0
    while(i<len(x) and j < len(y)):
        if x[i] != y[j]:
            skip += 1
            if(skip > 1):
                return False
            if len(x) > len(y):
                i += 1
            else:
                j += 1
        else:
            i +=1
            j += 1
    return True
def Test():
    test_set = [("",""),("", "x"),("x", ""),("x", "x"),("abcd", "eabcd"),("abcd", "aebcd"),("abcd", "abcde"),("xyz", "xz"),("yxz", "xz")]
    result_set = [False,True,True,False,True,True,True,True,True]
    i = 0
    for test in test_set:
        assert equalsWhenOneCharRemoved(test[0],test[1]) == result_set[i], "Incorrect Result %s,%s" % test
        i+=1
    print(len(test_set),"Tests passed successfully")
Test()
