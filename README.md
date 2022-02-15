[![Maintainability](https://api.codeclimate.com/v1/badges/7db766b24dfc3cd2ed5a/maintainability)](https://codeclimate.com/github/emp7yhead/py-organizer/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/7db766b24dfc3cd2ed5a/test_coverage)](https://codeclimate.com/github/emp7yhead/py-organizer/test_coverage) [![Check lint & tests](https://github.com/emp7yhead/py-organizer/actions/workflows/CI.yml/badge.svg)](https://github.com/emp7yhead/py-organizer/actions/workflows/CI.yml) [![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
# py-organizer
## Description:
CLI utilite for organizing files in current or chosen directory.
Currently work with ```.jpg```, ```.zip```, ```.mkv```, ```.pdf``` files.

Creates directories for files with the same extension and moves files into them.

## Dependencies:
- python = "^3.9"
- alive-progress = "^2.3.1"
## Usage:
```
usage: py-organizer [options] <dir>

Organizes files in current or chosen directory.

positional arguments:
  dir            directory to organize, default - current directory

optional arguments:
  -v, --version  show program's version number and exit
  -h, --help     dispaly help for command
```
## Installation:
Use the package manager pip:
```
pip install --user git+https://github.com/emp7yhead/py-organizer
```
### Or
Clone repository and use poetry:
```
git clone https://github.com/emp7yhead/py-organizer
cd py-organizer
make build
make package-install
```

### Work process:
#### In same directory:
<img src="https://media3.giphy.com/media/ZBOPlteu9XXKhA6Eqg/giphy.gif?cid=790b7611771b2c43ca2dad64a33b10a621c40f1897213e14&rid=giphy.gif&ct=g" width="640" height="480"/>

#### In chosen directory:
<img src="https://media0.giphy.com/media/0ctI05h8AwnRnfEt4i/giphy.gif?cid=790b76114321972fd643309cd15501f6e20106e8237ba272&rid=giphy.gif&ct=g" width="640" height="480"/>
