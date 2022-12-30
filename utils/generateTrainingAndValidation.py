import os
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import shutil


labels_dir = "alllabels"
images_dir = "alldata"

trainig_labels_dir = "train/labels"
trainig_data_dir = "train/data"
val_labels_dir = "val/labels"
val_data_dir = "val/data"

# create dirs if not exist
isExist = os.path.exists(trainig_labels_dir)
if not isExist:
    os.makedirs(trainig_labels_dir)
isExist = os.path.exists(trainig_data_dir)
if not isExist:
    os.makedirs(trainig_data_dir)
isExist = os.path.exists(val_labels_dir)
if not isExist:
    os.makedirs(val_labels_dir)
isExist = os.path.exists(val_data_dir)
if not isExist:
    os.makedirs(val_data_dir)



# get labels
filename_list = []
filename_list = os.listdir(labels_dir)

print(f"Number of labels: {len(filename_list)}")

# split data
indices = range(len(filename_list))
indices = np.asarray(indices)
labels_train, labels_validation, y1, y2 = train_test_split(indices, indices, test_size=0.3)

print(f"Number of train: {len(labels_train)}")
print(f"Number of val: {len(labels_validation)}")

# move data train
for id in labels_train:
    if filename_list[id] == "classes.txt":
        continue
    original = labels_dir + "/" + filename_list[id]
    target = trainig_labels_dir + "/" + filename_list[id]
    shutil.copyfile(original, target)
    original = images_dir + "/" + os.path.splitext(filename_list[id])[0] + ".png"
    target = trainig_data_dir + "/" + os.path.splitext(filename_list[id])[0] + ".png"
    shutil.copyfile(original, target)

# move data val
for id in labels_validation:
    if filename_list[id] == "classes.txt":
        continue
    original = labels_dir + "/" + filename_list[id]
    target = val_labels_dir + "/" + filename_list[id]
    shutil.copyfile(original, target)
    original = images_dir + "/" + os.path.splitext(filename_list[id])[0] + ".png"
    target = val_data_dir + "/" + os.path.splitext(filename_list[id])[0] + ".png"
    shutil.copyfile(original, target)