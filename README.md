# A tiny Python library for configuration
## Basic usage
```python:main.py
from argparse import ArgumentParser
import yaml

import tiny_conf as tc

parser = ArgumentParser()
parser.add_argument("config", type=str)
parser.add_argument("workspace", type=str)
args = parser.parse_args()

with open(args.config) as f:    
    config = vars(args) | tc.Struct(yaml.load(f, yaml.SafeLoader))

print("=" * 80)
print('Parameters')
print("-" * 80)
print(config)
print("=" * 80)

model = tc.instantiate(config.model)
optimizer = tc.instantiate(config.optimizer, params=model.parameters())

```
```yaml:config.ymal
num_epoch: 200
batch_size: 32

loss:
  _target_: torch.nn.BCELoss

model:
  _target_: foo_bar_model.FooBarModel
  hidden_size: 64
  num_layers: 5

optimizer:
  _target_: torch.optim.Adam
  lr: 1.e-3
```

```sh
$ python main.py config.yaml ./checkpoint_path/
```
<img src="assets/print_results.png" width=512>
