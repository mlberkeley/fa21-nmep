import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision import transforms
from torch.utils.data.dataset import Dataset  # For custom datasets
from data_pytorch import Data
from rotnet import RotNet
import time
import shutil
import yaml

parser = argparse.ArgumentParser(description='Configuration details for training/testing rotation net')
parser.add_argument('--config', type=str, required=True)
parser.add_argument('--train', action='store_true')
parser.add_argument('--data_dir', type=str, required=True)
parser.add_argument('--image', type=str)
parser.add_argument('--model_number', type=str, required=True)

args = parser.parse_args()

config = yaml.load(open(args.config, 'r'), Loader=yaml.FullLoader)


def train(train_loader, model, criterion, optimizer, epoch):
    model.train()
    for i, (input, target) in enumerate(train_loader):
    	#TODO: use the usual pytorch implementation of training

def validate(val_loader, model, criterion):
	model.eval()
    for i, (input, target) in enumerate(val_loader):
    	#TODO: implement the validation. Remember this is validation and not training
    	#so some things will be different.

def save_checkpoint(state, best_one, filename='rotationnetcheckpoint.pth.tar', filename2='rotationnetmodelbest.pth.tar'):
	torch.save(state, filename)
	#best_one stores whether your current checkpoint is better than the previous checkpoint
    if best_one:
        shutil.copyfile(filename, filename2)

def main():
	n_epochs = config["num_epochs"]
	model = #make the model with your paramters
	criterion = #what is your loss function
	optimizer = #which optimizer are you using

	train_dataset = #how will you get your dataset
	train_loader = #how will you use pytorch's function to build a dataloader
	val_loader = #how will you get your dataset
	val_loader = #how will you use pytorch's function to build a dataloader

	 for epoch in range(n_epochs):
	 	 #TODO: make your loop which trains and validates. Use the train() func

	 	 #TODO: Save your checkpoint





if __name__ == "__main__":
    main()
