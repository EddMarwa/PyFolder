import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 2)

    def forward(self, x):
        return self.fc(x)

model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    # forward, backward, optimize
    outputs = model(torch.randn(5, 10))
    loss = criterion(outputs, torch.randint(0, 2, (5,)))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

