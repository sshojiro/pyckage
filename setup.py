from setuptools import setup
import pyckage

__version__ = pyckage.__version__

install_requires = []

packages = [
    'pyckage',
    'pyckage.submodule',
    'pyckage_cli',
]

console_scripts = [
    'pyckage_cli=pyckage_cli.app:main'
]

setup(
    name='pyckage',
    version=__version__,
    packages=packages,
    install_requires=install_requires,
    entry_points={'console_scripts': console_scripts},
)
