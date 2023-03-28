import warnings

raise warnings.warn('This processing script is based on MATLAB.')

# testmask = load('OverlappingCCISC/Dataset/Synthetic/testset_GT.mat');
# trainmask = load('OverlappingCCISC/Dataset/Synthetic/trainset_GT.mat');

# num_test = length(testmask.CellNum);
# num_train = length(trainmask.CellNum);
# trainmask_cyto = trainmask.train_Cytoplasm;
# trainmask_nuclei = trainmask.train_Nuclei;
# testmask_cyto = testmask.test_Cytoplasm;
# testmask_nuclei = testmask.test_Nuclei;

# for i = 1:num_train
#     mask_nuclei = uint8(trainmask_nuclei{i});

#     num_cyto = length(trainmask_cyto{i});
#     [height, width] = size(trainmask_cyto{i}{1});
#     masks_tmp = zeros(height, width, num_cyto);
#     for j = 1:num_cyto
#         masks_tmp(:, :, j) = uint8(trainmask_cyto{i}{j});
#     end
#     mask_cyto = sum(masks_tmp, 3);
#     mask_cyto = uint8(min(mask_cyto, 1));
#     mask_cyto = mask_cyto + mask_nuclei;
#     disp([min(mask_cyto,[],'all'), max(mask_cyto,[],'all')])

#     path_cyto = [...
#             'OverlappingCCISC/masks/train/', 'synthetic_train_',...
#             num2str(i,'%03d'), '.png'];

#     imwrite(mask_cyto, path_cyto)
# end

# for i = 1:90
#     mask_nuclei = uint8(testmask_nuclei{i});

#     num_cyto = length(testmask_cyto{i});
#     [height, width] = size(testmask_cyto{i}{1});
#     masks_tmp = zeros(height, width, num_cyto);
#     for j = 1:num_cyto
#         masks_tmp(:, :, j) = uint8(testmask_cyto{i}{j});
#     end
#     mask_cyto = sum(masks_tmp, 3);
#     mask_cyto = uint8(min(mask_cyto, 1));
#     mask_cyto = mask_cyto + mask_nuclei;
#     disp([min(mask_cyto,[],'all'), max(mask_cyto,[],'all')])

#     path_cyto = [...
#         'OverlappingCCISC/masks/val/', 'synthetic_val_',...
#         num2str(i,'%03d'), '.png'];
#         imwrite(mask_cyto, path_cyto)
# end

# for i = 91:num_test
#     mask_nuclei = uint8(testmask_nuclei{i});

#     num_cyto = length(testmask_cyto{i});
#     [height, width] = size(testmask_cyto{i}{1});
#     masks_tmp = zeros(height, width, num_cyto);
#     for j = 1:num_cyto
#         masks_tmp(:, :, j) = uint8(testmask_cyto{i}{j});
#     end
#     mask_cyto = sum(masks_tmp, 3);
#     mask_cyto = uint8(min(mask_cyto, 1));
#     mask_cyto = mask_cyto + mask_nuclei;
#     disp([min(mask_cyto,[],'all'), max(mask_cyto,[],'all')])

#     path_cyto = [...
#         'OverlappingCCISC/masks/test/', 'synthetic_test_',...
#         num2str(i,'%03d'), '.png'];
#         imwrite(mask_cyto, path_cyto)
# end
