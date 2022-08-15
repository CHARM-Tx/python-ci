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

```conf
[mypy]
python_version = $your_version
files = $your_package

[tool:pytest]
addopts = --cov=$your_package
```

Once you've done all that, you should be able to call these like you would any action:

`uses: CHARM-Tx/python-ci/workflows/lint.yml`

See `full_run.yml` for an example of calling these workflows in a reusable way.

Note that instead of `uses: ./.github...` you'll have to use `CHARM-Tx/python-ci/.github...@$version`

Where `$version` is the latest version at the time you're writing your CI. You could use `main`
but this runs the risk that changes to the CI repo will break your workflow.

See the `.yml` files in `.github/workflows` for alternative call arguments.

## Local Development Environment

```bash
conda create -n python-ci --file environment.lock python=3.9
pip install -e .[tests]
```

If you update any of `lint/mypy/test` it's probably worth also updating the relevant
section in `python-release`.
