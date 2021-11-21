#순서의index를  보여주는게 아니고, 입력한 값대로 배정순을 보여주어야함.) -> 해결
names = ["azad","andy","louis","will","edward"]	


homes = [[3,4],[-1,5],[-4,4],[3,4],[-5,0]]

grades = [4.19, 3.77, 4.41, 3.65, 3.58]

def solution( names, homes, grades):
    home_list = []
    stu_list= []
    if len(names)==1:
        return [1]
    for i in range(len(homes)):
        home_list.append(homes[i][0]**2+homes[i][1]**2)
        stu_list.append([names[i], home_list[i], int(grades[i])])


    answers = sorted(stu_list, key = lambda x : x[0])

    answers = sorted(answers , key = lambda x : (-x[2], -x[1]))
    

    answer = []
    print(answers)
    for i in range(len(answers)):
        answer.append(answers[i][0])
    print(answer)
    ys = []
    for i in range(len(answers)):
        ys.append(answer.index(names[i]) + 1)


    return ys

print(solution(names, homes, grades))