#coding=utf-8

import os,sys,subprocess

py_ver = subprocess.check_output('python -V',shell=True)

if '3.10' in str(py_ver):

    os.system('pkg upgrade python -y')

    os.system('python X.py')

else:pass

current_os=subprocess.check_output('uname -om',shell=True)

if 'aarch64' in str(current_os):

    os.system('chmod 777 v19pro')

    os.system('./v19pro')

elif 'arm' in str(current_os):

   os.system('chmod 777 v19')

    os.system('./v19')

else:

    print('\n  Unknown device, aarch or os found, contact author.')

    os.sys.exit()
