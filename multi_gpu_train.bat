setx NGPUS "1"
setx CUDA_VISIBLE_DEVICES "0"
setx OMP_NUM_THREADS "32"
setx WORLD_SIZE "1"
setx PL_TORCH_DISTRIBUTED_BACKEND "gloo"

python -m torch.distributed.run --nproc_per_node=%NGPUS% tools/train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"

pause
