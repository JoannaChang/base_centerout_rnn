'''
Quick overview/outline for working with RNNs. Demonstration for students.
'''
#RNN class: networks.py
from asyncio import Task

#RNN class: networks.py
class RNN(nn.Module):
    '''Class for RNN to model neural dynamics and motor output'''
    def __init__():
        return None

    def forward ():
        #loop through time
        return None

#Task data class: task_data.py
class Task_Dataset(Dataset):
    """Centerout reach task dataset."""
    def __init__(self):
        self.data = []
        return None
        
    def __len__(self):
        len = 10
        return len

    def __getitem__(self, idx):
        return self.data[idx]

#Pipeline

#set up all hyper params
config = []

#set up data
data = Task_Dataset()

#create model, optimizer, and criterion
model = RNN()
optimizer = ... #SGD, Adam 
criterion = ... #MSE

#load weights
state_dict = ...
model.load_state_dict(state_dict)

#train
model.train()
for input, target in DataLoader(dataset...):
    optimizer.zero_grad()
    output = model(input)
    loss = criterion(output, target)
    #regularization

    loss.backward()
    optimizer.step()

#test
#load model
model.eval()
with torch.no_grad():
    testoutput = model(testinput)



