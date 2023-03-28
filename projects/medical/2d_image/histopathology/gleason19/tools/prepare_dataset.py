import glob
import os

import numpy as np
from PIL import Image
from scipy import mode

root_path = 'data/'
img_suffix = '.jpg'
seg_map_suffix = '.png'
save_img_suffix = '.png'
save_seg_map_suffix = '.png'
src_img_train_dir = os.path.join(root_path, 'Gleason/Train Imgs/Train Imgs')
src_img_test_dir = os.path.join(root_path, 'Gleason/Train Imgs/Test_imgs')

tgt_img_train_dir = os.path.join(root_path, 'images/train/')
tgt_img_test_dir = os.path.join(root_path, 'images/test/')
average_mask_dir = os.path.join(root_path, 'masks_average/train')
os.system('mkdir -p ' + tgt_img_train_dir)
os.system('mkdir -p ' + tgt_img_test_dir)
os.system('mkdir -p ' + average_mask_dir)


def filter_suffix_recursive(src_dir, suffix):
    # filter out file names and paths in source directory
    suffix = '.' + suffix if '.' not in suffix else suffix
    file_paths = glob.glob(
        os.path.join(src_dir, '**', '*' + suffix), recursive=True)
    file_names = [_.split('/')[-1] for _ in file_paths]
    return sorted(file_paths), sorted(file_names)


def convert_pics_into_pngs(src_dir, tgt_dir, suffix, convert='RGB'):
    if not os.path.exists(tgt_dir):
        os.makedirs(tgt_dir)

    src_paths, src_names = filter_suffix_recursive(src_dir, suffix=suffix)
    for i, (src_name, src_path) in enumerate(zip(src_names, src_paths)):
        tgt_name = src_name.replace(suffix, save_img_suffix)
        tgt_path = os.path.join(tgt_dir, tgt_name)
        num = len(src_paths)
        img = np.array(Image.open(src_path))
        if len(img.shape) == 2:
            pil = Image.fromarray(img).convert(convert)
        elif len(img.shape) == 3:
            pil = Image.fromarray(img)
        else:
            raise ValueError('Input image not 2D/3D: ', img.shape)

        pil.save(tgt_path)
        print(f'processed {i+1}/{num}.')


def adjust_missing_1(mask):
    # original masks contain no pixel of value 1,
    # e.g., having a range of [0, 2, 3, ...],
    # which needs to be addressed.
    mask_new = mask - 1
    mask_new[mask == 0] = 0
    mask_new[mask == 1] = 1
    return mask_new


convert_pics_into_pngs(src_img_train_dir, tgt_img_train_dir, suffix=img_suffix)

convert_pics_into_pngs(src_img_test_dir, tgt_img_test_dir, suffix=img_suffix)

for i in range(1, 6 + 1):
    mask_folder_name = 'Maps' + str(i) + '_T'
    src_mask_dir = f'data/Gleason/{mask_folder_name}/{mask_folder_name}'
    tgt_mask_dir = f'data/masks_{i}/train/'
    if not os.path.exists(tgt_mask_dir):
        os.makedirs(tgt_mask_dir)
    for mask_name in os.listdir(src_mask_dir):
        src_mask_path = os.path.join(src_mask_dir, mask_name)
        tgt_mask_name = mask_name.replace('_classimg_nonconvex', '')
        tgt_mask_path = os.path.join(tgt_mask_dir, tgt_mask_name)
        src_mask = np.array(Image.open(src_mask_path))
        tgt_mask = adjust_missing_1(src_mask)
        Image.fromarray(tgt_mask).save(tgt_mask_path)

all_mask_names = dict()
for i in range(1, 6 + 1):
    mask_dir = f'data/masks_{i}/train'
    all_mask_names[i] = sorted(os.listdir(mask_dir))

# average mask generation
for img_name in os.listdir(src_img_train_dir):
    img_name = img_name.replace('.jpg', '.png')
    mask_list = []
    count = 0
    for i in range(1, 6 + 1):
        current_mask_dir = f'data/masks_{i}/train'
        current_mask_names = all_mask_names[i]
        if img_name in current_mask_names:
            mask_path = os.path.join(current_mask_dir, img_name)
            mask = np.array(Image.open(mask_path))
            mask_list.append(mask)
            count += 1

    if count > 1:
        mask_average_path = os.path.join(average_mask_dir, img_name)
        print('Saving: ', mask_average_path)
        mask_average, _ = mode(mask_list)
        mask_average = mask_average[0]
        Image.fromarray(mask_average).save(mask_average_path)
    elif count == 1:
        mask_average_path = os.path.join(average_mask_dir, img_name)
        print('Saving: ', mask_average_path)
        mask_average = mask_list[0]
        Image.fromarray(mask_average).save(mask_average_path)
    else:
        print('No mask?: ', img_name)
