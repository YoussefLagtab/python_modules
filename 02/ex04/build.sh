echo \# upgrading pip, wheel and setuptools
pip3 install --upgrade pip setuptools where

echo \# bulding the package
python3 -m build
