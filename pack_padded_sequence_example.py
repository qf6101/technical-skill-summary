
# coding: utf-8

# ## This an example of using pytorch's pack_padded_sequence

# In[209]:


import numpy as np
import torch
from torch.autograd import Variable
from torch.nn.utils.rnn import pack_padded_sequence
from torch.nn.utils.rnn import pad_packed_sequence


# In[190]:


# create input data
# input size = 4
# seq size = [3, 1]
# batch size = 2
input = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 
            [[13, 14, 15, 16]]]


# In[191]:


# view input data values
input


# In[192]:


# lengths of sequences of input data
seq_lengths = torch.cuda.LongTensor(list(map(len, input)))


# In[193]:


# max length of sequences
seq_lengths.max()


# In[194]:


# create sequence tensor for multi-sequences (4 is input size)
seq_tensor = Variable(torch.zeros(len(input), seq_lengths.max(), 4))


# In[195]:


# view empty sequence tensor
seq_tensor


# In[196]:


# fill sequence tensor tensor with the first sequence
seq_tensor[0, :3] = torch.FloatTensor(np.asarray(input[0]))


# In[197]:


# fill sequence tensor tensor with the second sequence
seq_tensor[1, :1] = torch.FloatTensor(np.asarray(input[1]))


# In[198]:


# view filled sequence tensor
seq_tensor


# In[199]:


# view shape of sequence tensor before transposing batch dimension and sequence dimension
seq_tensor.shape


# In[200]:


# view sequence tensor before transposing batch dimension and sequence dimension
seq_tensor


# In[201]:


# transpose batch dimension and sequence dimension before padding data
seq_tensor = seq_tensor.transpose(0,1)


# In[202]:


# view shape of sequence tensor after transposing batch dimension and sequence dimension
seq_tensor.shape


# In[203]:


# view sequence tensor after transposing batch dimension and sequence dimension
seq_tensor


# In[204]:


# pad sequence tensor for rnn/lstm/gru network (batch_first=True if no transposing)
padded_input = pack_padded_sequence(seq_tensor, seq_lengths.cpu().numpy(), batch_first=False)


# In[205]:


# view the padded result
padded_input


# In[206]:


# unpad sequence tensor after training rnn/lstm/gru (batch_first=True if no transposing)
unpadded, unpadded_shape = pad_packed_sequence(packed_input, batch_first=False)


# In[207]:


# view unpadded tensor
unpadded


# In[208]:


# view shape of unpadded tensor
unpadded_shape

