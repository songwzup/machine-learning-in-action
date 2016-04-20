# import math
# while 1:
#     inp = raw_input().strip().split()
#     f = int(inp[0])
#     result = 0.0
#     for i in range(1,int(inp[1])+1):
#         result += f
#         f = math.sqrt(f)
#     print '%.2f' % result



while 1:
    inp1=int(raw_input())
    inp2=int(raw_input())
    result=[]
    for i in range(inp1,inp2+1):
        b=i/100
        print b
        s=(i-i/100*100)/10
        print s
        g=i-i/100*100-i/10*10
        print g
        if i==b**3+s**3+g**3:
            result.append(i)
    if len(result)==0:
        print 'no'
    else:
        print ' '.join(map(str,result))