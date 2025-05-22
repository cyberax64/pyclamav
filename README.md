# PyClamAV

Python binding for the ClamAV antivirus engine.

## Description

This module provides a Python interface to the ClamAV virus scanning engine. It allows you to easily integrate virus scanning capabilities into your Python applications.

## Project Structure

```
pyclamav/
├── pyclamav/           # Python package
│   ├── src/            # C extension source code
│   ├── examples/       # Example scripts
│   ├── tests/          # Test suite
│   └── docs/           # Documentation
├── database/           # ClamAV virus database
├── include/            # ClamAV header files
├── openssl/            # OpenSSL header files
├── conf_examples/      # ClamAV configuration examples
├── setup.py            # Installation script
├── LICENSE             # License information
└── README.md           # This file
```

## Requirements

- Python 3.9 or newer (Python 3.12 recommended)
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

See `pyclamav/examples/example.py` for a more complete example including multi-threaded scanning.

## Documentation

Detailed API documentation is available in the `pyclamav/docs/` directory.

## Testing

Run the test suite with:

```bash
python -m unittest discover -s pyclamav/tests
```

## License

GPL