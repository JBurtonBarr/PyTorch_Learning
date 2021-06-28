import torch
import numpy as np
#torch will be reliant on the np datastructure for tensors

#We want to initialise our tensor by offering data to a numpy array and then parsing that array into torch

data = [[1, 2, 3],[3, 4, 5], [2, 2, 1],[5, 2, 3]]
#we could do torch_data = torch.tensor(data) this is more direct
# more often that not though our data will be in a numpy array

np_a = np.array(data)
tensor_np = torch.from_numpy(np_a) #good


#we can make a shape and datatype like tensor from another tensor
datashapeclone = torch.ones_like(tensor_np) #will be filled with 1's
#random clone 
datashapeclone_rand = torch.rand_like(tensor_np, dtype = torch.float)
