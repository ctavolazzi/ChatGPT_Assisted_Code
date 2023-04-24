import os
import importlib

class ModuleManager:
    def __init__(self, module_dir=None):
        if module_dir is None:
            module_dir = os.path.dirname(__file__)
        self.module_dir = module_dir
        self.modules = {}
        self.name = '"ModuleManager: ' + module_dir + '"'
        self._load_modules(module_dir)

    def _load_modules(self, directory):
        print(f"Loading modules from: {directory}")
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".py"):
                    module_name = filename[:-3]
                    module_path = os.path.join(dirpath, filename)
                    module = importlib.import_module(module_path.replace("/", ".")[:-3])
                    self.modules[module_name] = module

    def set_name(self, name):
        self.name = name
        return self

    def run(self):
        print(f"Running {self.name}...")
        print('Modules:')
        print(self.modules.items())
        for module_name, module in self.modules.items():
            if hasattr(module, "setup"):
                print(f"Running setup for {module_name}...")
                module.setup()


if __name__ == '__main__':
    mm = ModuleManager("TestFunctions")
    mm.set_name("ModuleManager_main")

    print(mm.name)
    print(mm.modules)