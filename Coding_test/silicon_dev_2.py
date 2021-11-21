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

    print(stu_list)
    answers = sorted(stu_list, key = lambda x : x[0])

    answers = sorted(answers , key = lambda x : (-x[2], -x[1]))
    
  

    # print(answers)
    
    answer = []
    for i in range(len(answers)):
        answer.append(names.index(answers[i][0]) + 1)


    return answer

print(solution(names, homes, grades))