
import torch.nn as nn
#add imports as necessary

class ResNet:

    def __init__(self, block, layers, num_classes=1000):
        super(ResNet, self).__init__()
        #populate the layers with your custom functions or pytorch
        #functions.
        self.conv1 = 
        self.bn1 = 
        self.relu = 
        self.maxpool = 
        self.layer1 = 
        self.layer2 = 
        self.layer3 = 
        self.layer4 = 
        self.avgpool = 
        self.fc = 


    def forward(self, x):
        #TODO: implement the forward function for resnet,
        #use all the functions you've made


    def new_block(self, in_planes, out_planes, stride):
        layers = []
        #TODO: make a convolution with the above params
        return nn.Sequential(*layers)