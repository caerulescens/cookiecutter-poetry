# {{ cookiecutter.name }}

{{ cookiecutter.description }}

## Install

| Name                                                   |
|--------------------------------------------------------|
| [poetry](https://github.com/python-poetry)             |
| [pre-commit](https://github.com/pre-commit/pre-commit) |

Development:
```shell
poetry install
poetry shell
pre-commit install
```

Production:
```shell
poetry install --without dev
```

## Usage

Package:
```shell
poetry build
```

Run:
```shell
poetry run {{ cookiecutter.__distribution_name }}
```

Test:
```shell
pytest .
```

Check:
```shell
pre-commit run
```
