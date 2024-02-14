# Build executable
python setup.py build

# Remove cf_Freeze license
Remove-Item -Path ./build/bigid-catalog-email-objects-reporting/frozen_application_license.txt

# Create application zip for deployment
Set-Location ./build
Compress-Archive -Path ./bigid-catalog-email-objects-reporting -DestinationPath ./bigid-catalog-email-objects-reporting.zip