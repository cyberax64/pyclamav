#!/usr/bin/env python3
"""
Example script demonstrating the use of pyclamav for virus scanning.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import pyclamav
import glob
import os
import sys


def main():
    # Print ClamAV version
    print(f"ClamAV Version: {pyclamav.get_version()}")
    
    # Set database path
    db_path = 'database'
    if not os.path.exists(db_path):
        print(f"Error: Database directory '{db_path}' not found.")
        print("Please download the ClamAV virus database first.")
        sys.exit(1)
    
    # Load the virus database
    print(f"Loading database from '{db_path}'...")
    result = pyclamav.load_database(db_path)
    if result != 0:
        print("Error loading database.")
        sys.exit(1)
    
    # Print number of virus signatures
    print(f"Loaded {pyclamav.get_numsig()} virus signatures")
    
    # Function to scan a single file
    def scan_file(filepath):
        try:
            result, virus_name = pyclamav.scanfile(filepath)
            if result == 1:
                return (filepath, True, virus_name)
            else:
                return (filepath, False, None)
        except Exception as e:
            return (filepath, None, str(e))
    
    # Scan files in parallel
    print("\nScanning files...")
    files_to_scan = list(glob.glob('*.*', recursive=True))
    
    if not files_to_scan:
        print("No files found to scan.")
        sys.exit(0)
    
    print(f"Found {len(files_to_scan)} files to scan")
    
    results = []
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as executor:
        future_to_file = {executor.submit(scan_file, file): file for file in files_to_scan}
        for future in as_completed(future_to_file):
            results.append(future.result())
    
    # Print results
    print("\nScan Results:")
    print("-" * 60)
    
    clean_files = 0
    infected_files = 0
    error_files = 0
    
    for filepath, is_infected, details in results:
        if is_infected is None:
            print(f"ERROR: {filepath} - {details}")
            error_files += 1
        elif is_infected:
            print(f"INFECTED: {filepath} - {details}")
            infected_files += 1
        else:
            clean_files += 1
    
    print("-" * 60)
    print(f"Summary: {clean_files} clean, {infected_files} infected, {error_files} errors")


if __name__ == "__main__":
    main()