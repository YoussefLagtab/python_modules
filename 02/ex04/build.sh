echo \# upgrading pip, wheel and setuptools
pip3 install --upgrade pip setuptools where

echo \# bulding the package
python3 -m build

echo \# installing the package
pip install ./dist/my_minipack-1.0.0.tar.gz