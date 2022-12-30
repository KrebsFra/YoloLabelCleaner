# YoloLabelCleaner
This tool can be used to unify Yolo labels to a consistent set in case of different classes.txt.
The application is described using the labeling tool (https://pypi.org/project/labelImg/). 
It is assumed that the images are in the directory "images_dir" and the current labels including the associated _classes.txt_ are in "labels_dir".
"images_dir" and "labels_dir" are exemplary and can be replaced with the local directory names.
Further there should be a file called _classes_desired.txt_ including an ordered list of all labels present in the data (corresponding to class name list in yolo). If you do not have _classes.txt_ anymore copy and rename _classes_desired.txt_ to _classes.txt_. In this case _classes.txt_ should be adapted during checking the current labels.

## Check current labels
Open labelImg using:
```
labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
or in our case:
```
labelImg images_dir labels_dir/classes.txt
```

Open "change save dir" and select labels_dir and double click at a file in file list. Now you can go over the frames and check if the labels are correct.
If not adapt the classes.txt and check again.


## Apply pythong script
Execute the script and pass the _current_dir_ as the directory containing the current labels and _output_dir_ as the directory where the new labels should be placed. For our example this could be:
```
python generateCorrectLabels.py --current_dir labels_dir --output_dir labels_dir_new
```

## Check new labels
Open labelImg using:
```
labelImg images_dir labels_dir_new/classes.txt
```
Open "change save dir" and select labels_dir_new and double click at a file in file list. Now you can go over the frames and check if the new labels are correct.

## Apply on full data
This procedure can be applied on multiple datasets. If the same _classes_desired.txt_ is used the generated data can be used as a consistent dataset for training yolo.


(The script was tested for Python 3.10.9)
