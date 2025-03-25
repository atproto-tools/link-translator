import importlib
import os

modules_names = [name for name in os.listdir('handlers') if name.endswith('.py') and not name.startswith('_')]
modules = [importlib.import_module("handlers." + name[:-3]) for name in sorted(modules_names)]

code_template = """
{0}

handlers_lookup = {{\n{1}}}
""".removeprefix("\n")

if __name__ == "__main__":
    imports = ""
    handlers_lookup_contents = ""
    for module in modules:
        handler_name = module.__name__.split(".")[-1]
        imports += (f"from {module.__name__} import handler as {handler_name}\n")
        for host in module.hosts:
            handlers_lookup_contents += f'    "{host}": {handler_name},\n'

    with open("handlers_lookup.py", "w") as f:
        f.write(code_template.format(imports, handlers_lookup_contents))
