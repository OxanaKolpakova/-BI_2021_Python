Windows 10 Pro
Python 3

Instructions for installing third party python libraries 

1) The third party python libraries required to run pain.py successfully
 are specified in the requirements.txt file.

2) You can download and install them from anaconda by running the following script:

virtualenv --python=3.8 packet_sniffer_env38
conda update [-n root] -v anaconda
pip install --upgrade google-api-python-client
pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
pip install bs4
pip install Bio
pip install pandas
pip install scipy
pip install virtualenv
pip install --user scanpy
pip install opencv-python
pip install lxml
