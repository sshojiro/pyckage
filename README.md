Pyckage - Python Package Sample Project
===

## Packaging

```bash
$ python setup.py sdist
```

## Installation

```bash
$ python setup.py install
```

or after saving the `.tar.gz` under `dist/` directory,

```bash
$ pip install dist/pyckage-0.0.1.tar.gz
```

To uninstall it,

```bash
$ pip uninstall dist/pyckage-0.0.1.tar.gz
```

To install, you may do the following:

```bash
tar -xvzf pyckage-0.0.1.tar.gz
pip install pyckage-0.0.1
python setup.py install
```

## Command

```bash
$ PYTHONPATH=. python -c 'import pyckage; print(pyckage.Hoge()())'
$ PYTHONPATH=. python -c 'from pyckage.submodule import Piyo; print(Piyo()())'
```

Other commands are:

```bash
$ python -m pyckage_cli.app -n hoge
What is called was: Hoge
$ python -m pyckage_cli.app -n piyo
What is called was: Piyo
$ python -m pyckage_cli.app -n fuga
What is called was: Fuga
```
