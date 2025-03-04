import importlib
import pkgutil


def list_modules(package_name):
    package = importlib.import_module(package_name)
    modules = []
    for _, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
        modules.append(module_name)
        if is_pkg:
            modules.extend(list_modules(module_name))
    return modules


def test_check_isolated_domain_layer():
    accepted_layers = [
        "domain"
    ]
    root = 'src'
    modules = list_modules(root)
    for module in modules:
        imported_module = module.split('.')[1]
        for layer in accepted_layers:
            assert imported_module == layer, f"""Module "{module}" is not in accepted layer "{accepted_layers}" """


def test_check_isolated_application_layer():
    accepted_layers = [
        "domain",
        "application",
        "shared",
    ]
    root = 'src'
    modules = list_modules(root)
    for module in modules:
        imported_module = module.split('.')[1]
        for layer in accepted_layers:
            assert imported_module == layer, f"""Module "{module}" is not in accepted layer "{accepted_layers}" """


def test_check_isolated_presentation_layer():
    accepted_layers = [
        "application",
        "shared",
    ]
    root = 'src'
    modules = list_modules(root)
    for module in modules:
        imported_module = module.split('.')[1]
        for layer in accepted_layers:
            assert imported_module == layer, f"""Module "{module}" is not in accepted layer "{accepted_layers}" """


def test_check_isolated_infrastructure_layer():
    accepted_layers = [
        "application",
        "presentation",
        "shared",
    ]
    root = 'src'
    modules = list_modules(root)
    for module in modules:
        imported_module = module.split('.')[1]
        for layer in accepted_layers:
            assert imported_module == layer, f"""Module "{module}" is not in accepted layer "{accepted_layers}" """


def test_check_isolated_shared_layer():
    accepted_layers = [
        "shared",
    ]
    root = 'src'
    modules = list_modules(root)
    for module in modules:
        imported_module = module.split('.')[1]
        for layer in accepted_layers:
            assert imported_module == layer, f"""Module "{module}" is not in accepted layer "{accepted_layers}" """
