#! /bin/bash

# Find local (user) TDS tree
TEXMF_DEFAULT=${HOME}/texmf
TEXMFHOME=$(kpsewhich -var-value=TEXMFHOME)

# Define where are files should reside
SPROOT=${TEXMFHOME:-$TEXMF_DEFAULT}/tex/latex/sp
echo "Installing to ${SPROOT}"
echo

# List of files to be installed
FILES='sharedsp.sty beamersp.sty postersp.sty imagesc.py theme'

# Create directory in the local TDS treee (if it doesn't exist)
mkdir -p ${SPROOT}

# Copy files to the correct directory
cp -rv ${FILES} ${SPROOT}

# Create symlink for backwards compatibility

echo
echo "Symlinking beamersp2017.sty"
ln -sf ${SPROOT}/beamersp.sty ${SPROOT}/beamersp2017.sty
