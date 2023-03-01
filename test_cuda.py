import torch


print("这是一个检测cuda运算pytorch环境的脚本")


print(torch.cuda.is_available())

a = torch.ones((3,1))
a = a.cuda(0)
b = torch.ones((3,1)).cuda(0)
c = a+b
print(c)