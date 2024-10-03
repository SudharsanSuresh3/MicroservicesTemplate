import yaml

with open("./config/nameko_config.yaml") as f:
    nameko_config = yaml.safe_load(f)