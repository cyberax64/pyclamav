from setuptools import setup, Extension, find_packages
import shutil
import glob
import os

try:
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('pyclamav.egg-info')
except:
    pass
    
# Collect DLLs and other files
dlls = glob.glob(os.path.join('*.dll'))
openssl = glob.glob(os.path.join('openssl', '*.*'))
database = glob.glob(os.path.join('database', '*.*'))

# Define the extension module
pyclamav_extension = Extension(
    'pyclamav',
    sources=['pyclamav/src/pyclamav.c'], 
    libraries=['libclamav', 'python312'],
    library_dirs=['.'],
    include_dirs=['.']
)

# Read the long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyclamav',
    version='0.0.3',
    author='ELIZALDE Elodie',
    author_email='cyberax@protonmail.com',
    license='GPL',
    keywords="python, clamav, antivirus, scanner, virus, libclamav",
    url='https://github.com/cyberax64/pyclamav',
    description='Python binding for the ClamAV antivirus engine',
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules=[pyclamav_extension],
    packages=find_packages(),
    data_files=[
        ('', dlls), 
        ('database', database), 
        ('openssl', openssl)
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.9',
)