# cookiecutter-poetry

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for [`poetry`](https://github.com/python-poetry/poetry).

## Install

| Name                                                     |
|----------------------------------------------------------|
| [pyenv](https://github.com/pyenv/pyenv)                  |
| [poetry](https://github.com/python-poetry)               |
| [pre-commit](https://github.com/pre-commit/pre-commit)   |

Configure:
```shell
cat <<EOF > poetry.yaml
[virtualenvs]
create = true
in-project = true
prefer-active-python = true
EOF
poetry install
poetry shell
pre-commit install
```

## Usage

Run:
```shell
cookiecutter .
```

Test:
```shell
pytest .
```

Check:
```shell
pre-commit run
```
