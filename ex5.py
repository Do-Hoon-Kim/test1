# -*- coding: utf-8 -*-

num1 = 21
if num1 %3 == 0 and num1 %7 == 0:
    print '3의 배수이면서 7의배수'
elif num1 %3 == 0:
    print '3의 배수'
elif num1 %7 ==0:
    print '7의 배수'
else:
    print '3의배수도 7의배수도 아니다'
