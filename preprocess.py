import torch
import copy
import numpy as np
import matplotlib.pyplot as plt

mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)

def preprocess(x, mean, std):
    assert x.size(1) == 3
    y = torch.zeros_like(x)
    for i in range(3):
        y[:, i, :, :] = (x[:, i, :, :] - mean[i]) / std[i]
    return y


def preprocess_input_function(x):
    '''
    allocate new tensor like x and apply the normalization used in the
    pretrained model
    '''
    return preprocess(x, mean=mean, std=std)

def undo_preprocess(x, mean, std):
    assert x.size(1) == 3
    y = torch.zeros_like(x)
    for i in range(3):
        y[:, i, :, :] = x[:, i, :, :] * std[i] + mean[i]
    return y

def undo_preprocess_input_function(x):
    '''
    allocate new tensor like x and undo the normalization used in the
    pretrained model
    '''
    return undo_preprocess(x, mean=mean, std=std)

def save_preprocessed_img(fname, preprocessed_img):
    img_copy = copy.deepcopy(preprocessed_img)
    undo_preprocessed_img = undo_preprocess_input_function(img_copy)
    #print('image index {0} in batch'.format(index))
    undo_preprocessed_img = undo_preprocessed_img.cpu().numpy()
    undo_preprocessed_img = np.transpose(undo_preprocessed_img, [1,2,0])
    if fname:
        plt.imsave(fname, undo_preprocessed_img)
    return undo_preprocessed_img

def save_preprocessed_img2(fname, preprocessed_imgs, index):
    img_copy = copy.deepcopy(preprocessed_imgs)
    undo_preprocessed_img = undo_preprocess_input_function(img_copy)
    #print('image index {0} in batch'.format(index))
    undo_preprocessed_img = undo_preprocessed_img[index]
    undo_preprocessed_img = undo_preprocessed_img.detach().cpu().numpy()
    undo_preprocessed_img = np.transpose(undo_preprocessed_img, [1,2,0])
    
    plt.imsave(fname, undo_preprocessed_img)
    return undo_preprocessed_img
