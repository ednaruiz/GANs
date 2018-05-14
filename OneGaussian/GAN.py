
try:
  import torch
  import torch.nn as nn
  import torch.nn.functional as F
  
  import argparse
  import numpy
  
except ImportError,e:
  
  print e
  raise SystemExit
  
if __name__ == '__main__':
  
  parser = argparse.ArgumentParser("Train a GAN for generating 1D gaussian")
  parser.AddArgument( "-s" , "--sigma", help = "Sigma of the Gaussian", dest = "sigma", required = True, type = float)
  parser.AddArgument( "-m" , "--mean" , help = "Mean of the Gaussian", dest = "mean", required = True, type = float)
  
  try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
        
  
