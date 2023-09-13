# Real-time Scene Text Detection with Differentiable Binarization
**note**: these code is inherited from https://github.com/WenmuZhou/DBNet.pytorch
## Train
1. config the `dataset['train']['dataset'['data_path']'`,`dataset['validate']['dataset'['data_path']`in [config/icdar2015_resnet18_fpn_DBhead_polyLR.yaml](cconfig/icdar2015_resnet18_fpn_DBhead_polyLR.yaml)
## Test
[eval.py](tools/eval.py) is used to test model on test dataset
1. config `model_path` in [eval.sh](eval.sh)
## Predict 
[predict.py](tools/predict.py) Can be used to inference on all images in a folder
1. config `model_path`,`input_folder`,`output_folder` in [predict.sh](predict.sh)
## terminal command
1. conda activate dbnet_wenmu
2. cd C:\Application\Develop\DBNet_pytorch_Wenmu
3. python ./tools/train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"
4. python ./tools/predict.py --model_path ./output/DBNet_resnet18_FPN_DBHead/checkpoint/model_best.pth --input_folder ./input --output_folder ./output/inference --thre 0.3
