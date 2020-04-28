while(1):
    print('enter 1st no.')
    n1=int(input())
    print('enter the operant, for example:+,-,*,/,**')
    op=input()
    print('enter the 2nd no.')
    n2=int(input())
    if n1==45 and op=='*' and n2==3:
        print('555')
    elif n1==56 and op=='+' and n2==9:
        print('77')
    elif n1==56 and op=='/' and n2==6:
        print('4')
    elif op=='+':
        r=n1+n2
        print(r)
    elif op=='-':
        r=n1-n2
        print(r)    
    elif op=='*':
        r=n1*n2
        print(r)
    elif op=='/':
        r=n1/n2
        print(r)
    elif op=='**':
        r=n1**n2
        print(r)
