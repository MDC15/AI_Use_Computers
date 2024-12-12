# Function calling


def call_func(name, *args, **kwargs):
    """
    Call a function by name.
    """
    import importlib

    mod_name, func_name = name.rsplit(".", 1)
    mod = importlib.import_module(mod_name)
    func = getattr(mod, func_name)
    return func(*args, **kwargs)
