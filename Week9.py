import torch 
x = torch.tensor([[1, 2], [3, 4]])
print(x)
print(x.shape,x.dtype)

ones_tensor = torch.ones_like(x)
print(ones_tensor)
