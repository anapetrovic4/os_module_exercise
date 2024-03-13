import os
import shutil
import random

random.seed(44)

# Create new directories train, test and val
train = 'train'
test = 'test'
val = 'val'

# Create paths for parent folders
parent_images = '/mnt/c/projects/os_module_task/coco128-seg/images/train2017/'
parent_labels = '/mnt/c/projects/os_module_task/coco128-seg/labels/train2017/'

# Create paths for train, test and val
path_images_train = os.path.join(parent_images, train)
path_images_test = os.path.join(parent_images, test)
path_images_val = os.path.join(parent_images, val)

path_labels_train = os.path.join(parent_labels, train)
path_labels_test = os.path.join(parent_labels, test)
path_labels_val = os.path.join(parent_labels, val)

# Make directories
os.makedirs(path_images_train, exist_ok=True)
print("Directory '%s' created" % train)

os.makedirs(path_images_test, exist_ok=True)
print("Directory '%s' created" % test)

os.makedirs(path_images_val, exist_ok=True)
print("Directory '%s' created" % val)

os.makedirs(path_labels_train, exist_ok=True)
print("Directory '%s' created" % train)

os.makedirs(path_labels_test, exist_ok=True)
print("Directory '%s' created" % test)

os.makedirs(path_labels_val, exist_ok=True)
print("Directory '%s' created" % val)

#################################################################################

# Split files

# Copy from train2017 to train  - IMAGES
train_folder = '/mnt/c/projects/os_module_task/coco128-seg/images/train2017/train/'
train2017_files = [i for i in os.listdir(parent_images) if i.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

for file in train2017_files:
    shutil.copy(parent_images + file, train_folder + file)
    
# Delete from train2017 all files - IMAGES
for file in os.listdir(parent_images):
    if os.path.isfile(parent_images + file):
        os.remove(os.path.join(parent_images, file))

# Copy from train2017 to train - LABELS
train_folder_labels = '/mnt/c/projects/os_module_task/coco128-seg/labels/train2017/train/'
train2017_files_labels = [i for i in os.listdir(parent_labels) if i.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt'))]

for file in train2017_files_labels:
    shutil.copy(parent_labels + file, train_folder_labels + file)

# Delete from train2017 all files - LABELS
for file in os.listdir(parent_labels):
    if os.path.isfile(parent_labels + file):
        os.remove(os.path.join(parent_labels, file))
        
# Check mismatched files in images/train vs labels/train

# List files
train_images = [i for i in os.listdir(train_folder) if i.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
train_labels = [i for i in os.listdir(train_folder_labels) if i.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt'))]

# Extract image and labels names
image_names = [os.path.splitext(i)[0] for i in train_images]
labels_names = [os.path.splitext(i)[0] for i in train_labels]

mismatched_files_labels = []
mismatched_files_images = []

# laksi nacin??
for image_name in image_names:
    if image_name not in labels_names:
        mismatched_files_labels.append(image_name)
print('Labels with these names do not exist: ')
print(mismatched_files_labels)

for label_name in labels_names:
    if label_name not in image_names:
        mismatched_files_images.append(label_name)
print('Images with these names do not exist: ')
print(mismatched_files_images)

# Delete mismatched files
if os.path.exists(train_folder_labels + '000000000656.txt' or train_folder_labels + '000000000659.txt'
                  or train_folder + '000000000250.jpg' or train_folder + '000000000508.jpg'):
    os.remove(os.path.join(train_folder_labels, '000000000656.txt'))
    os.remove(os.path.join(train_folder_labels, '000000000659.txt'))
    os.remove(os.path.join(train_folder, '000000000250.jpg'))
    os.remove(os.path.join(train_folder, '000000000508.jpg'))
else:
    print('Files are deleted')

# Copy 10% from train to test - IMAGES
num_to_select = int(len(train_images) * 0.1)

test_images = random.sample(train_images, num_to_select)

for image in test_images:
    src_path = os.path.join(path_images_train, image)
    dest_path = os.path.join(path_images_test, image)
    
    shutil.copy(src_path, dest_path)
    os.remove(src_path)

# Update image files to exclude test images - ne razumem
train_images = [i for i in train_images if i not in test_images]

val_images = random.sample(train_images, num_to_select)

for image in val_images:
    src_path = os.path.join(path_images_train, image)
    dest_path = os.path.join(path_images_val, image)
    
    shutil.copy(src_path, dest_path)
    os.remove(src_path)
    
# Copy 10% from train to test - LABELS
num_to_select_labels = int(len(train_labels) * 0.1)

test_labels = random.sample(train_labels, num_to_select_labels)

for label in test_labels:
    src_path = os.path.join(path_labels_train, label)
    dest_path = os.path.join(path_labels_test, label)
    
    shutil.copy(src_path, dest_path)
    os.remove(src_path)

# Update image files to exclude test images - ne razumem
train_labels = [i for i in train_labels if i not in test_labels]

val_labels = random.sample(train_labels, num_to_select_labels)

for label in val_labels:
    src_path = os.path.join(path_labels_train, label)
    dest_path = os.path.join(path_labels_val, label)
    
    shutil.copy(src_path, dest_path)
    os.remove(src_path)