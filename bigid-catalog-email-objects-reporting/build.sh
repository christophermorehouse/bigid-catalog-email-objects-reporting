#!/bin/bash

python3 setup.py build_exe

# Remove cf_Freeze license
rm build/cbigid-catalog-email-objects-reporting/frozen_application_license.txt

# Create application tarball for deployment
cd build
tar -zcvf bigid-catalog-email-objects-reporting.tar.gz bigid-catalog-email-objects-reporting