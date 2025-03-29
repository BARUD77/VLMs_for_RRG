import torch
import pytorch_lightning as pl

print("Torch Version:", torch.__version__)
print("CUDA Available:", torch.cuda.is_available())
print("PyTorch Lightning Version:", pl.__version__)
