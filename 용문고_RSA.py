import time
def gcd(a, b):
    if a>=b :
        while b > 0:
            a, b = b, a % b
        return a
    else :
        while a > 0:
            b, a = a, b % a
        return b

def lcm(a, b):
     return a * b / gcd(a, b)

p_dict={'A':97, 'B':103, 'C':109, 'D':113, 'E':131}    
while True :
    print("정해진 문자가 입력되지 않을 시 종료됩니다")
    print("선택한 방을 알파벳 순으로 하나씩 차례대로 입력하세요(A,B,C,D,E)")
    print("예:A, C 선택 시")
    print("A")
    print("C")
    
    p=input()
    q=input()
    
    if p=='A':
        p=p_dict['A']
    elif p=='B':
        p=p_dict['B']
    elif p=='C':
        p=p_dict['C']
    elif p=='D':
        p=p_dict['D']
    elif p=='E':
        p=p_dict['E']
    
    if q=='A':
        q=p_dict['A']
    elif q=='B':
        q=p_dict['B']
    elif q=='C':
        q=p_dict['C']
    elif q=='D':
        q=p_dict['D']
    elif q=='E':
        q=p_dict['E']
    
    N=p*q
    L=lcm(p-1, q-1)
    L=int(L)
    G=2
    l=[]
    while G<L :
        if gcd(L,G)==1:
                l.append(G)
        G=G+1
    if p in l :
        l.remove(p)
    if q in l :
        l.remove(q)
    G=l[len(l)-1]
    #print(G)
    for i in range(1,L):
        if (i*G)%L==1 :
            F=i
            break
    #공개키
    def rsa_e(a):
        return (a**G)%N
    #비밀키
    def rsa_d(a):
        return (a**F)%N
    
    print("번호 순서대로 문제의 답을 입력하세요")
    print("예: A, C 선택 시, 각 답이 123, 345라면 ")
    print("1 2 3 3 4 5")
    user=input()
    user_list=user.split(' ')
    for i in range(len(user_list)-1,0,-1):
        print(rsa_e(int(user_list[i])), end='')
        
    print()
    if p==97 and q==103 :
        print("정답은 832679932498666149961입니다")
    elif p==97 and q==109 :
        print("정답은 881163447930704952871입니다")
    elif p==97 and q==113 :
        print("정답은 182787698221365454811입니다")
    elif p==97 and q==131 :
        print("정답은 211850833177423663541입니다")
    elif p==103 and q==109 :
        print("정답은 935644912807748556141입니다")
    elif p==103 and q==113 :
        print("정답은 194023282910388058201입니다")
    elif p==103 and q==131 :
        print("정답은 2249809610120449867471입니다")
    elif p==109 and q==113 :
        print("정답은 205349279238410661591입니다")
    elif p==109 and q==131 :
        print("정답은 238028563570476071401입니다")
    elif p==113 and q==131 :
        print("정답은 1233688823701986974021입니다")
    
    print("답이 다르다면 문제를 다시 풀어보세요")
    print("이 화면을 캡쳐해주시고 아래 메일주소로 보내주세요")
    print("comfox707@gmail.com")
    print("'종료'라고 입력해주세요")
    ans=input()
    if ans=="종료":
        break
    else :
        print("다른 거 입력하지 마세요")
        print("5초 후 종료됩니다")
        time.sleep(5)
        break
