def main(n) :
    big_num_list = []
    match_tent = []
    pre_match_tent = []
    ans = []
    for _ in range(n) :
        number = input()
        big_num_list.append(number.split(" "))
    for i in big_num_list :
        for j in big_num_list:
            if i == j :
                pass
            elif (abs(int(i[0]) - int(j[0]))) == abs(int(i[1]) - int(j[1])) :
                if i not in match_tent and j not in match_tent :
                    pre_match_tent.append(i)
                    pre_match_tent.append(j)
                    match_tent.append(pre_match_tent)
                    pre_match_tent = []
                else :
                    pass
            else :
                pass
    if match_tent == [] :
        print("0")
    else :
        for i in match_tent:
            width = abs(int(i[0][0]) - int(i[1][0]))
            ans.append(width)
        print(max(ans))
main(int(input()))
