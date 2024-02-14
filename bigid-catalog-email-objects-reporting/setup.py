# This script was created by cx_Freeze with the following command: cxfreeze-quickstart
# cx_Freeze is a tool that turns python scripts into standalone executable binaries.
# Project page: https://pypi.org/project/cx-Freeze/
# Project documentation: https://cx-freeze.readthedocs.io/en/latest/

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'build_exe': 'build/bigid-catalog-email-objects-reporting', 
    'packages': [], 
    'excludes': [], 
    'include_files': ['env_config.yaml']
}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'bigid-catalog-email-objects-reporting')
]

setup(name='bigid-catalog-email-objects-reporting',
      version = '1.0',
      description = 'bigid-catalog-email-objects-reporting',
      options = {'build_exe': build_options},
      executables = executables)