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

A good practice is to use a python virtual environment, so that each project has it own environment at does not share a python configuration. **Venv must not be pushed !**

1. Create a virtual env:
```
$ python3 -m venv venv
```

2. Add `venv*` path to [gitignore](https://github.com/OctaveLauby/ProjectModel/blob/master/.gitignore).

3. Activate venv
```
$ source venv/bin/activate
```

4. Install requirements
```
(venv) $ pip install -r requirements.txt
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


## Syntaxes

The way you write code must be **consistent** along the project, or at least in every package.

Something you have to respect is the [PEP8 coding conventions](https://www.python.org/dev/peps/pep-0008/).

Then you can draw your inspiration from [Google conventions](https://google.github.io/styleguide/pyguide.html).

A best way to improve and build a good coding styles is to regulary read code of others (standard libraries are a good way to start).



# Use case


## Main

**Script**: [play.py](https://github.com/OctaveLauby/ProjectModel/blob/master/play.py)

**Description**: Launch game implemented in [gaming.games](https://github.com/OctaveLauby/ProjectModel/tree/master/gaming/games/)

**Usage**: `$ python3 play.py -h`

**Examples**:
```
$ python3 play.py Dummy
$ python3 play.py Dummy -b 0
$ python3 play.py Dummy --loglvl DEBUG --p_loglvl DEBUG --p_logpath logs/dummy_players.log
```


## More

Launch tests using command (Linux):
```
$ sh run_tests.sh
```

Launch linter on a package:
```
$ pylint <package_name> --ignore tests --init-hook="import sys; sys.path.append('.')"
```
