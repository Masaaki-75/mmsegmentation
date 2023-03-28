# 2019 Automatic Gleason grading of prostate cancer in digital histopathology

## Description

This project supportss **`2019 Automatic Gleason grading of prostate cancer in digital histopathology `**, which can be downloaded from [here](https://gleason2019.grand-challenge.org/Register/).

### Dataset Overview

Prostate Cancer (PCa) is the sixth most common and second deadliest cancer among men worldwide. There exist various techniques for PCa detection and staging. However, microscopic inspection of stained biopsy tissue by expert pathologists is the most accurate method. Based on the observable histological patterns, each region of the tissue is assigned a Gleason grade of 1 to 5. The final Gleason score is reported as the sum of the most prominent and second most prominent patterns; e.g., a tissue with the most prominent pattern of Gleason grade of 4 and the second most prominent pattern of Gleason grade of 3 will have a Gleason score of 4+3.

This challenge aims at the automatic Gleason grading of prostate cancer from H&E-stained histopathology images. This task is of critical importance because Gleason score is a strong prognostic predictor. On the other hand, it is very challenging because of the large degree of heterogeneity in the cellular and glandular patterns associated with each Gleason grade, leading to significant inter-observer variability, even among expert pathologists.

Gleason grading of prostate cancer is usually performed via visual inspection (with a microscope) of the prostate tissue by expert pathologists. However, this is a time-consuming task and suffers from very high inter-observer variability. Automatic computer-aided methods have the potential for improving the speed, accuracy, and reproducibility of the results.

### Original Statistic Information

| Dataset name                                                   | Anatomical region | Task type    | Modality       | Num. Classes | Train/Val/Test Images | Train/Val/Test Labeled | Release Date | License                                                   |
| -------------------------------------------------------------- | ----------------- | ------------ | -------------- | ------------ | --------------------- | ---------------------- | ------------ | --------------------------------------------------------- |
| [Gleason19](https://gleason2019.grand-challenge.org/Register/) | pelvis            | segmentation | histopathology | 5            | 244/-/87              | yes/-/no               | 2019         | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

|   Class Name    | Num. Train | Pct. Train | Num. Val | Pct. Val | Num. Test | Pct. Test |
| :-------------: | :--------: | :--------: | :------: | :------: | :-------: | :-------: |
|   background    |    244     |   55.86    |    -     |    -     |     -     |     -     |
|     benign      |    101     |    4.89    |    -     |    -     |     -     |     -     |
| gleason grade 3 |    142     |   15.95    |    -     |    -     |     -     |     -     |
| gleason grade 4 |    171     |   22.75    |    -     |    -     |     -     |     -     |
| gleason grade 5 |     16     |    0.54    |    -     |    -     |     -     |     -     |

Note:

- `Pct` means percentage of pixels in this category in all pixels.

### Visualization

![gleason19](https://raw.githubusercontent.com/uni-medical/medical-datasets-visualization/main/2d/semantic_seg/histopathology/gleason19/gleason19_dataset.png)

### Dataset Citation

```
@article{Nir2018AutomaticGO,
  title={Automatic grading of prostate cancer in digitized histopathology images: Learning from multiple experts},
  author={Guy Nir and Soheil Hor and Davood Karimi and Ladan Fazli and Brian F. Skinnider and Peyman Tavassoli and Dmitry Turbin and Carlos F. Villamil and G. Wang and R. Storey Wilson and Kenneth A. Iczkowski and M. Scott Lucia and Peter C. Black and Purang Abolmaesumi and S. Larry Goldenberg and Septimiu E. Salcudean},
  journal={Medical Image Analysis},
  year={2018},
  volume={50},
  pages={167–-180}
}

@article{8853320,
  title={Deep Learning-Based Gleason Grading of Prostate Cancer From Histopathology Images—Role of Multiscale Decision Aggregation and Data Augmentation},
  author={Karimi, Davood and Nir, Guy and Fazli, Ladan and Black, Peter C. and Goldenberg, Larry and Salcudean, Septimiu E.},
  journal={IEEE Journal of Biomedical and Health Informatics},
  year={2020},
  volume={24},
  number={5},
  pages={1413-1426}
}
```

### Prerequisites

- Python v3.8
- PyTorch v1.10.0
- pillow(PIL) v9.3.0 v9.3.0
- scikit-learn(sklearn) v1.2.0 v1.2.0
- [MIM](https://github.com/open-mmlab/mim) v0.3.4
- [MMCV](https://github.com/open-mmlab/mmcv) v2.0.0rc4
- [MMEngine](https://github.com/open-mmlab/mmengine) v0.2.0 or higher
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) v1.0.0rc5

All the commands below rely on the correct configuration of `PYTHONPATH`, which should point to the project's directory so that Python can locate the module files. In `gleason19/` root directory, run the following line to add the current directory to `PYTHONPATH`:

```shell
export PYTHONPATH=`pwd`:$PYTHONPATH
```

### Dataset Preparing

- download dataset from [here](https://gleason2019.grand-challenge.org/Register/) and decompress data to path `'data/'`.
- run script `python tools/prepare_dataset.py` to format data and change folder structure as below.
- run script `python ../../tools/split_seg_dataset.py` to split dataset and generate `train.txt`, `val.txt` and `test.txt`. If the label of official validation set and test set cannot be obtained, we generate `train.txt` and `val.txt` from the training set randomly.

```none
  mmsegmentation
  ├── mmseg
  ├── projects
  │   ├── medical
  │   │   ├── 2d_image
  │   │   │   ├── histopathology
  │   │   │   │   ├── gleason19
  │   │   │   │   │   ├── configs
  │   │   │   │   │   ├── datasets
  │   │   │   │   │   ├── tools
  │   │   │   │   │   ├── data
  │   │   │   │   │   │   ├── train.txt
  │   │   │   │   │   │   ├── val.txt
  │   │   │   │   │   │   ├── images
  │   │   │   │   │   │   │   ├── train
  │   │   │   │   |   │   │   │   ├── xxx.png
  │   │   │   │   |   │   │   │   ├── ...
  │   │   │   │   |   │   │   │   └── xxx.png
  │   │   │   │   │   │   ├── masks
  │   │   │   │   │   │   │   ├── train
  │   │   │   │   |   │   │   │   ├── xxx.png
  │   │   │   │   |   │   │   │   ├── ...
  │   │   │   │   |   │   │   │   └── xxx.png
```

### Divided Dataset Information

***Note: The table information below is divided by ourselves.***

|   Class Name    | Num. Train | Pct. Train | Num. Val | Pct. Val | Num. Test | Pct. Test |
| :-------------: | :--------: | :--------: | :------: | :------: | :-------: | :-------: |
|   background    |    195     |   56.16    |    49    |  54.67   |     -     |     -     |
|     benign      |     80     |    4.96    |    21    |   4.64   |     -     |     -     |
| gleason grade 3 |    116     |   16.49    |    26    |  13.79   |     -     |     -     |
| gleason grade 4 |    133     |   21.73    |    38    |  26.84   |     -     |     -     |
| gleason grade 5 |     13     |    0.66    |    3     |   0.05   |     -     |     -     |

### Training commands

To train models on a single server with one GPU. (default)

```shell
mim train mmseg ./configs/${CONFIG_FILE}
```

### Testing commands

To test models on a single server with one GPU. (default)

```shell
mim test mmseg ./configs/${CONFIG_FILE}  --checkpoint ${CHECKPOINT_PATH}
```

<!-- List the results as usually done in other model's README. [Example](https://github.com/open-mmlab/mmsegmentation/tree/dev-1.x/configs/fcn#results-and-models)

You should claim whether this is based on the pre-trained weights, which are converted from the official release; or it's a reproduced result obtained from retraining the model in this project. -->

## Results

### 2019 Automatic Gleason grading of prostate cancer in digital histopathology

|     Method      | Backbone | Crop Size |   lr   | mIoU  | mDice |                                     config                                     |         download         |
| :-------------: | :------: | :-------: | :----: | :---: | :---: | :----------------------------------------------------------------------------: | :----------------------: |
| fcn_unet_s5-d16 |   unet   |  512x512  |  0.01  | 76.48 | 84.68 |  [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.01-20k_gleason19-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.001  | 61.06 | 63.69 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.001-20k_gleason19-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.0001 | 58.87 | 62.42 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.0001-20k_gleason19-512x512.py) | [model](<>) \| [log](<>) |

## Checklist

- [x] Milestone 1: PR-ready, and acceptable to be one of the `projects/`.

  - [x] Finish the code
  - [x] Basic docstrings & proper citation
  - [x] Test-time correctness
  - [x] A full README

- [x] Milestone 2: Indicates a successful model implementation.

  - [x] Training-time correctness

- [ ] Milestone 3: Good to be a part of our core package!

  - [ ] Type hints and docstrings
  - [ ] Unit tests
  - [ ] Code polishing
  - [ ] Metafile.yml

- [ ] Move your modules into the core package following the codebase's file hierarchy structure.

- [ ] Refactor your modules into the core package following the codebase's file hierarchy structure.
