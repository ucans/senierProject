import os
import torch


use_cuda = torch.cuda.is_available()

default_checkpoint = {
    "epoch": 0,
    "train_losses": [],
    "train_symbol_accuracy": [],
    "train_sentence_accuracy": [],
    "train_wer": [],
    "validation_losses": [],
    "validation_symbol_accuracy": [],
    "validation_sentence_accuracy": [],
    "validation_wer": [],
    "lr": [],
    "grad_norm": [],
    "model": {},
    "configs":{},
    "token_to_id":{},
    "id_to_token":{},
}


def save_checkpoint(checkpoint, dir="./checkpoints", prefix=""):
    # save model
    filename = "{num:0>4}.pth".format(num=checkpoint["epoch"])
    if not os.path.exists(os.path.join(prefix, dir)):
        os.makedirs(os.path.join(prefix, dir))
    torch.save(checkpoint, os.path.join(prefix, dir, filename))


def load_checkpoint(path, cuda=use_cuda):
    if cuda:
        return torch.load(path)
    else:
        # Load GPU on CPU
        return torch.load(path, map_location=lambda storage, loc: storage)

