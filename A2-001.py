def main(num,point1,point2) :
    cut = 1
    num_list = num.split(" ")
    laser_bounce_1 = point1.split(" ")
    laser_bounce_2 = point2.split(" ")
    if int(num_list[0]) <= int(num_list[1]) :
        for i in laser_bounce_2 :
            time = 0
            n = 0
            m = 1
            while time <= int(num_list[0]) :
                if int(i) > int(laser_bounce_1[-1]) or int(i) < int(laser_bounce_1[0]) :
                    break
                if int(laser_bounce_1[n]) <= int(i) <= int(laser_bounce_1[m]) :
                    cut += 1
                    break
                else :
                    n += 1
                    m += 1
                time += 1
    else :
        for i in laser_bounce_1 :
            time = 0
            n = 0
            m = 1
            while time <= int(num_list[1]) :
                if int(i) > int(laser_bounce_2[-1]) or int(i) < int(laser_bounce_2[0]) :
                    break
                if int(laser_bounce_2[n]) <= int(i) < int(laser_bounce_2[m]) :
                    cut += 1
                    break
                else :
                    n += 1
                    m += 1
                time += 1
    print(cut)
main(input(),input(),input())