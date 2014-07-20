# iPhone Messages Exporter

This script will examine the iTunes backup directory to find the most recent backup. Once discovered, it will organized the backups in the backup directory based on the handle. The logs are of the format: "Date - handle: message".

## Installing

Should make use of the python standard library only. Written using python 2.7.6.

## Preparation

Before running this script, you must backup your iDevice with iTunes.

## Running

Simply clone this codebase, cd into the directory, and run ```python imessage-exporter.py```. By default the backups should be located in the ```backup``` directory.
