from argparse import ArgumentParser
import yaml

import tiny_conf as tc

parser = ArgumentParser()
parser.add_argument("config", type=str)
parser.add_argument("--arg1", type=str)
parser.add_argument("--arg2", type=str)
args = parser.parse_args()

with open(args.config) as f:    
    config = vars(args) | tc.Struct(yaml.load(f, yaml.SafeLoader))

print("=" * 80)
print('Parameters')
print("-" * 80)
print(config)
print("=" * 80)