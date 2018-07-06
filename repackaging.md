# How to repackage an executable version

Windows:

1. Ensure you have all the regular dependencies (found in requirements.md) and also: pip install cx_freeze. 

2. Fil out the information in setup.py with the acurate information to reflect the changes. 

3. When ready to repackage run: python setup.py build

OSX:

Not supported for packaging atm
