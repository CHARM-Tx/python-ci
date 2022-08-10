# python-ci
A repository for generally useful Python CI workflows

## Requirements for Use

- A conda `environment.lock` (it can be empty if you like; your Python is included automatically)
- A minimal `setup.py` that just calls `setup()`
- A `setup.cfg` file (see the one in this repo for reference) specifying:
    - The usual metadata
    - Dependencies via `install_requires`
    - Test dependencies via `extra_requires`
    - The following sections:

Once you've done all that, you should be able to call these like you would any action:

`uses: CHARM-Tx/python-ci/workflows/lint.yml`

```conf
[mypy]
python_version = $your_version
files = $your_package

[tool:pytest]
addopts = --cov=$your_package
```

## Local Development Environment

```bash
conda create -n python-ci --file environment.lock python=3.9
pip install -e .[tests]
```