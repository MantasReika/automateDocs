@echo off
echo Generating python file...
python -m PyQt5.uic.pyuic -x MainView.ui -o MainView.py
echo Done.
pause