Model Of Python3 Project
---


# Introduction

This project is a good example of how to frame its own project.

## Architecture

Basically the structure of a project should be as the following:
```
\ (root)
\ .gitignore
\ requirements.txt
\ README.md
\ main.py or main.sh

\ package_i \
\ package_i \ __init__.py
\ package_i \ module_i_j.py
\ package_i \ module_i_k \
\ package_i \ module_i_k \ ... (same as package)

\ package_i \ tests \
\ package_i \ tests \ __init__.py
\ package_i \ tests \ test_module_i_j.py
\ package_i \ tests \ test_module_i_k \
\ package_i \ tests \ test_module_i_k \ ...
```


## Tests

I like to use pytest as it is simple to use.

## Environment

A good practice is to use a python virtual environment, so that each project has it own environment at does not share a python configuration.

1. Create a virtual env:
```
$ python3 -m venv venv
```

2. Add `venv*` path to .gitignore.

3. Activate venv
```
$ source venv/bin/activate
```

4. Install requirements
```
(venv) $ pip install -r requirements
```

5. Leave environment:
```
(venv) $ deactivate
```


> Why is it a problem to share a python config ?
>
> - project A use the version v1 of a library
> - project B use the version v2
> - v1 and v2 are not compatible
> - You can't launch both projects at the same time



# Use case

## Main

**Script**: main.py

**Description**: not implemented yet

**Usage**: `$ python3 main.py -h`

**Examples**: not implemented yet


## More

Launch tests using command (Linux):
```
$ sh run_tests.sh
```

Launch linter on a package:
```
$ pylint <package_name> --ignore tests --init-hook="import sys; sys.path.append('.')"
```
