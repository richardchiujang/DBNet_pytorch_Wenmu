REM activate conda env trainocr 
call C:\anaconda3\Scripts\activate.bat C:\anaconda3
call conda activate trainocr
cd C:\develop\DBNet_pytorch_Wenmu

python tools\train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"
REM python tools\train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"
REM python tools\train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"
REM python tools\train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"