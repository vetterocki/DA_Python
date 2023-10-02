def create(function_locals):
    return {var.capitalize(): value for var, value in function_locals.items()}


def joined(some_dict):
    return "\n".join([f"{k}:\n{v}\n" for k, v in some_dict.items()])
