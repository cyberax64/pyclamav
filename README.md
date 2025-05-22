# PyClamAV

Python binding for the ClamAV antivirus engine.

## Description

This module provides a Python interface to the ClamAV virus scanning engine. It allows you to easily integrate virus scanning capabilities into your Python applications.

## Requirements

- Python 3.12
- ClamAV (Version: 0.105.0 or newer)
- ClamAV virus database

## Installation

### Option 1: Install from pre-compiled package

Copy the compiled version to your Python's Lib\site-packages directory.

### Option 2: Compile from source

```bash
python setup.py install
```

**Note:** Make sure to download the virus database into the 'database' folder before using.

## Usage

```python
import pyclamav

# Load the virus database
pyclamav.load_database('path/to/database')

# Get ClamAV version
print("ClamAV Version:", pyclamav.get_version())

# Get number of virus signatures
print("Number of signatures:", pyclamav.get_numsig())

# Scan a file
result, virus_name = pyclamav.scanfile('file_to_scan.exe')
if result == 1:
    print(f"Virus detected: {virus_name}")
else:
    print("No virus found")
```

See `example.py` for a more complete example including multi-threaded scanning.

## License

GPL
