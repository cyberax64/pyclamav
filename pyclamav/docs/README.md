# PyClamAV Documentation

## Overview

PyClamAV is a Python binding for the ClamAV antivirus engine. This documentation provides information on how to use the library.

## API Reference

### `load_database(path)`

Sets the path to the ClamAV virus database.

**Parameters:**
- `path` (string): Path to the database directory

**Returns:**
- `0` on success, error code otherwise

### `scanfile(filename)`

Scans a file for viruses.

**Parameters:**
- `filename` (string): Path to the file to scan

**Returns:**
- A tuple `(status, virus_name)` where:
  - `status`: `0` when no virus is found, `1` if a virus is detected
  - `virus_name`: Name of the detected virus (empty string if no virus)

**Exceptions:**
- `ValueError`: If an error occurs during scanning
- `TypeError`: If wrong arguments are passed

### `check_database_file(filename)`

Checks if a database file can be correctly compiled.

**Parameters:**
- `filename` (string): Path to the database file

**Returns:**
- `CL_SUCCESS` if it can be compiled successfully

### `get_numsig()`

Gets the number of known virus signatures.

**Parameters:**
- None

**Returns:**
- Number of known signatures (integer)

### `get_version()`

Gets the ClamAV version.

**Parameters:**
- None

**Returns:**
- ClamAV version (string)