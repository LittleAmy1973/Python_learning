'''计算正数平方根
num = float(input('请输入一个数字：'))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))


#计算负数或者实数的平方根
import cmath

num = int(input("请输入一个数字："))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根是{1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real, num_sqrt.imag))
'''

num = float(input('请输入一个数字：'))
num_sqrt = num ** 0.5
print(' %0.2f 的平方根为 %0.2f'%(num, num_sqrt))

