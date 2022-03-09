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
