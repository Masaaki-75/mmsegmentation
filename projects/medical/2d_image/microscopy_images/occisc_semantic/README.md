# Overlapping Cervical Cytology Image Segmentation Challenge (OCCISC, semantic seg version)

## Description

This project supportss **`Overlapping Cervical Cytology Image Segmentation Challenge (OCCISC, semantic seg version) `**, which can be downloaded from [here](https://gleason2019.grand-challenge.org/Register/).

### Dataset Overview

The automated detection and segmentation of overlapping cells using microscopic images obtained from Pap smear can be considered to be one of the major hurdles for a robust automatic analysis of cervical cells. The Pap smear is a screening test used to detect pre-cancerous and cancerous processes, which consists of a sample of cells collected from the cervix that are smeared onto a glass slide and further examined under a microscope. The main factors affecting the sensitivity of the Pap smear test are the number of cells sampled, the overlap among these cells, the poor contrast of the cell cytoplasm, and the presence of mucus, blood and inflammatory cells. Automated slide analysis techniques attempt to improve both sensitivity and specificity by automatically detecting, segmenting and classifying the cells present on a slide.

In this challenge, the targets are to extract the boundaries of individual cytoplasm and nucleus from overlapping cervical cytology images.

### Original Statistic Information

| Dataset name                                                         | Anatomical region | Task type    | Modality          | Num. Classes | Train/Val/Test Images | Train/Val/Test Labeled | Release Date | License                                             |
| -------------------------------------------------------------------- | ----------------- | ------------ | ----------------- | ------------ | --------------------- | ---------------------- | ------------ | --------------------------------------------------- |
| [Occisc-semantic](https://gleason2019.grand-challenge.org/Register/) | not_human         | segmentation | microscopy_images | 3            | 45/90/810             | yes/yes/yes            | 2014         | [unknown](https://creativecommons.org/publicdomain) |

| Class Name | Num. Train | Pct. Train | Num. Val | Pct. Val | Num. Test | Pct. Test |
| :--------: | :--------: | :--------: | :------: | :------: | :-------: | :-------: |
| background |     45     |   73.32    |    90    |  85.82   |    810    |   85.60   |
| cytoplasm  |     45     |   26.01    |    90    |  13.20   |    810    |   13.43   |
|   nuclei   |     45     |    0.67    |    90    |   0.98   |    810    |   0.97    |

Note:

- `Pct` means percentage of pixels in this category in all pixels.

### Visualization

![occisc_semantic](https://raw.githubusercontent.com/uni-medical/medical-datasets-visualization/main/2d/semantic_seg/microscopy_images/occisc_semantic/occisc_semantic_dataset.png)

### Dataset Citation

```
@ARTICLE{7005499,
  author={Lu, Zhi and Carneiro, Gustavo and Bradley, Andrew P.},
  journal={IEEE Transactions on Image Processing},
  title={An Improved Joint Optimization of Multiple Level Set Functions for the Segmentation of Overlapping Cervical Cells},
  year={2015},
  volume={24},
  number={4},
  pages={1261-1272},
  doi={10.1109/TIP.2015.2389619}}

@ARTICLE{7386573,
  author={Lu, Zhi and Carneiro, Gustavo and Bradley, Andrew P. and Ushizima, Daniela and Nosrati, Masoud S. and Bianchi, Andrea G. C. and Carneiro, Claudia M. and Hamarneh, Ghassan},
  journal={IEEE Journal of Biomedical and Health Informatics},
  title={Evaluation of Three Algorithms for the Segmentation of Overlapping Cervical Cells},
  year={2017},
  volume={21},
  number={2},
  pages={441-450},
  doi={10.1109/JBHI.2016.2519686}}

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

All the commands below rely on the correct configuration of `PYTHONPATH`, which should point to the project's directory so that Python can locate the module files. In `occisc_semantic/` root directory, run the following line to add the current directory to `PYTHONPATH`:

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
  │   │   │   ├── microscopy_images
  │   │   │   │   ├── occisc_semantic
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

### Overlapping Cervical Cytology Image Segmentation Challenge (OCCISC, semantic seg version)

|     Method      | Backbone | Crop Size |   lr   | mIoU  | mDice |                                        config                                        |         download         |
| :-------------: | :------: | :-------: | :----: | :---: | :---: | :----------------------------------------------------------------------------------: | :----------------------: |
| fcn_unet_s5-d16 |   unet   |  512x512  |  0.01  | 76.48 | 84.68 |  [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.01-20k_occisc-semantic-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.001  | 61.06 | 63.69 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.001-20k_occisc-semantic-512x512.py)  | [model](<>) \| [log](<>) |
| fcn_unet_s5-d16 |   unet   |  512x512  | 0.0001 | 58.87 | 62.42 | [config](./configs/fcn-unet-s5-d16_unet_1xb16-0.0001-20k_occisc-semantic-512x512.py) | [model](<>) \| [log](<>) |

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
