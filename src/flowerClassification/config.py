from box import Box

import yaml


with open('params.yaml', 'r') as file:
    data = yaml.safe_load(file)
    config = Box(data)


print(config)


