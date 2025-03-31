import yaml


def write_yaml(content: dict, fname: str) -> None:
    """write yaml."""
    with open(fname, "w") as stream:
        yaml.dump(content, stream, indent=2, sort_keys=False)
