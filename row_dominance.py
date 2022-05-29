def binding(a,b):   #한자리수만 다른 수끼리 묶기
    char = ''
    cnt = 0
    for num in range(len(a)):
        if a[num] == b[num]:
            char += a[num]
        else:
            char += '-'
            cnt += 1
    
    if cnt > 1:
        return None
    elif cnt == 1:
        return char
#============================
def cmp(a,b):   #minterm과 pi비교
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
        elif a[i] == '1' and b[i] == '-':
            cnt+=1
        elif a[i] == '-' and b[i] == '1':
            cnt+=1
        elif a[i] == '0' and b[i] == '-':
            cnt+=1
        elif a[i] == '-' and b[i] == '0':
            cnt+=1
        else:
            continue
            
        
    if cnt == len(a):
        return 'right'
    else:
        return 'wrong'


#===============
def sorting(a,b,c):
    for i in a:
        temp=i.replace('-','2')
        b.append(temp)
    b.sort()
    for j in b:
        temp=j.replace('2','-')
        c.append(temp)
    

#=============================
def solution(minterm):
    answer = []
    var_size = minterm[0]   # 변수 개수
    min_num = minterm[1]   #minterm  개수
    del minterm[0:2]  #앞에 두정보 제외하고 나머지를 minterm으로 저장
    original_minterm = [] 
    can_PI = []   #PI 후보 저장
    tmp = [] #임시저장
    used = []
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    epi =[]
    
    
    
    for num in range(0, 2**(var_size)):
        if num in minterm:
            can_PI.append(format(num,'b').zfill(var_size))#PI후보들 bin형태로 저장함
            original_minterm.append(format(num,'b').zfill(var_size))
            
    while True:
        cnt=0
        for i in range(len(can_PI)):
            for j in range(i+1,len(can_PI)):
                k = binding(can_PI[i],can_PI[j])
                if k != None:
                    if k not in tmp:
                        
                        tmp.append(k)
                        cnt += 1
                        if can_PI[i] not in used:
                            used.append(can_PI[i])
                        if can_PI[j] not in used:    
                            used.append(can_PI[j])
                    elif k in tmp :
                        cnt += 1
                        if can_PI[i] not in used:
                            used.append(can_PI[i])
                        if can_PI[j] not in used:    
                            used.append(can_PI[j])
                
                else:
                    continue
        if cnt != 0:
            for num in used:
                if num in can_PI:
                    can_PI.remove(num)
                    for x in tmp:
                        if x not in can_PI:
                            can_PI.append(x)
                            tmp.remove(x)
                    
                            continue
        
        else:
            sorting(can_PI,a1,a2)
            break

    row = len(original_minterm)
    col = len(a2)
    epi_test =[[None]* col for i in range(row)]
    for i in original_minterm:
        for j in a2:
            epi_test[original_minterm.index(i)][a2.index(j)] = cmp(i,j)
    
    for x in range(len(original_minterm)):
        if epi_test[x].count('right') == 1:
            for y in range(len(a2)):
                if cmp(original_minterm[x],a2[y]) == 'right':
                    j = a2[y]
                    if j not in a3:
                        a3.append(j)

                
            
    sorting(a3,a4,epi)
        
    epi.insert(0,'EPI')

    #=========================
    #      Row dominance
    #=========================

    row_checklist = [[]for i in range(len(a2))]
    for x in a2:
        row_checklist[a2.index(x)].append(x)
        for y in original_minterm:
            if cmp(x,y) == 'right':
                row_checklist[a2.index(x)].append(y)
    
    row_checklist2 = []
    for x in range(len(a2)):
        list1 = row_checklist[x]
        list2 = list1[1:]
        row_checklist2.append(list2)
    
    row_dominant = []

    for x in range(len(row_checklist2)):
        for y in range(x+1,len(row_checklist2)):
            cmp_list1 = row_checklist2[x]
            cmp_list2 = row_checklist2[y]
            intersection = list(set(cmp_list1) & set(cmp_list2))
            if intersection == cmp_list1 and intersection not in row_dominant:
                row_dominant.append(intersection)
            elif intersection == cmp_list2 and intersection not in row_dominant:
                row_dominant.append(intersection)

    answer = row_dominant

    return answer


#EOF
