"""
PyClamAV - Python binding for the ClamAV antivirus engine.
"""

try:
    from pyclamav import (
        load_database,
        scanfile,
        check_database_file,
        get_numsig,
        get_version
    )
except ImportError:
    # If the C extension is not available, provide dummy functions for documentation
    def load_database(path):
        """
        Sets the path to the ClamAV virus database.
        
        Args:
            path (str): Path to the database directory
            
        Returns:
            int: 0 on success, error code otherwise
        """
        raise NotImplementedError("PyClamAV C extension not available")
    
    def scanfile(filename):
        """
        Scans a file for viruses.
        
        Args:
            filename (str): Path to the file to scan
            
        Returns:
            tuple: (status, virus_name) where status=0 when no virus found or status=1 if virus detected
            
        Raises:
            ValueError: If an error occurs during scanning
            TypeError: If wrong arguments are passed
        """
        raise NotImplementedError("PyClamAV C extension not available")
    
    def check_database_file(filename):
        """
        Checks if database file can be correctly compiled.
        
        Args:
            filename (str): Path to the database file
            
        Returns:
            int: CL_SUCCESS if it can be compiled successfully
        """
        raise NotImplementedError("PyClamAV C extension not available")
    
    def get_numsig():
        """
        Gets the number of known virus signatures.
        
        Returns:
            int: Number of known signatures
        """
        raise NotImplementedError("PyClamAV C extension not available")
    
    def get_version():
        """
        Gets the ClamAV version.
        
        Returns:
            str: ClamAV version
        """
        raise NotImplementedError("PyClamAV C extension not available")

__version__ = "0.0.3"