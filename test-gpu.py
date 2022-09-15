import torch

flag = torch.cuda.is_available()
if flag:
    print("CUDA可使用")
else:
    print("CUDA不可用")

print(torch.cuda.device_count())

print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_name(1))
