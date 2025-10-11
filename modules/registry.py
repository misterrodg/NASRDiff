FILE_REGISTRY = {}


def register_faa_file(key):
    def decorator(cls):
        FILE_REGISTRY[key] = cls
        return cls

    return decorator
