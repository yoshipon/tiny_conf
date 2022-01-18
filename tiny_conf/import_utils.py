from importlib import import_module


def import_and_getattr(name):
    module_name, attr_name = name.rsplit(".", 1)
    return getattr(import_module(module_name), attr_name)


def instantiate(config, **kwargs):
    Cls = import_and_getattr(config._target_)
    return Cls(**config.popped("_target_"), **kwargs)
