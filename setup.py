from distutils.core import setup, Extension
import shutil
import glob
import os

try:
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('pyclamav.egg-info')
except:
    pass
    
    
dlls     = glob.glob(os.path.join('*.dll'))
openssl  = glob.glob(os.path.join('openssl', '*.*'))
database = glob.glob(os.path.join('database', '*.*'))


pyclamav = Extension(
    'pyclamav',
    sources      = ['pyclamav.c'], 
    libraries    = ['libclamav', 'python39'],
    library_dirs = ['.']
)

# Build : python setup.py build
# Install : python setup.py install
# Register : python setup.py register

#  platform = 'Unix',
#  download_url = 'https://github.com/donfucius/pyclamav/tree/mypyclamav',


setup (
    name             = 'pyclamav',
    version          = '0.0.2',
    author           = 'ELIZALDE Elodie',
    author_email     = 'cyberax@protonmail.com',
    license          ='GPL',
    keywords         ="python, clamav, antivirus, scanner, virus, libclamav",
    url              = 'https://github.com/donfucius/pyclamav',
    include_dirs     = ['.'],
    data_files       = [('', dlls), ('database', database), ('openssl', openssl)],
    description      = 'This is a python binding to the C libclamav library (from the Clamav project - http://www.clamav.net) based on http://xael.org/norman/python/pyclamav/. It can be used to easily allow a Python script to scan a file against known viruses.',
    long_description = 'This is a python binding to the C libclamav library (from the Clamav project - http://www.clamav.net) based on http://xael.org/norman/python/pyclamav/. It can be used to easily allow a Python script to scan a file against known viruses.',
    ext_modules      = [pyclamav]
)
