import importlib.util
import sys
import typing
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType


def dynamic_import(module: "typing.Union[str, Path]") -> "ModuleType":
	"""
	Dynamically import a python module

	Args:
		module (Path): Path to the module to import

	Returns:
		Module: The imported module
	"""
	module = Path(module)
	spec: "ModuleSpec" = importlib.util.spec_from_file_location(module.stem, str(module))  # type: ignore
	mod = importlib.util.module_from_spec(spec)
	sys.modules[module.name] = mod

	spec.loader.exec_module(mod) # type: ignore
	return mod
