#!/bin/bash
echo "Unzipping files..."
unzip public-transport-traffic-data-in-france.zip

echo "Deleting unnecessary files..."
rm *ation*
rm *.zip