# runcsv-minimal

This is a minimal implementation of the `runcsv` system, which allows to use a CSV file as a python-powered spreadsheet.

## Installing

You need to clone the [runcsv](https://github.com/yassirnajmaoui/runcsv) module repository first somewhere in your files.

Then you need to add a symbolic link in this folder like

```
ln -s /path/to/runcsv ./
```

## Usage

Usage of `main.py` is as follows:

```
usage: python main.py [-h] [-i I] [-o O]

Process a CSV file

optional arguments:
  -h, --help  show this help message and exit
  -i I        Input csv file
  -o O        Output csv file
```

This will take a CSV file, interpret it as the `s` layer, process the whole spreadsheet left-right top-bottom, and output the `f` layer
