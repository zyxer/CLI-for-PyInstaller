#-*- coding:utf-8 -*-
__author__ = "lwalenl aka GreenUA"

import os
import subprocess
import Tkinter, tkFileDialog


version = "v.0.1 - *beta*-chanel"
root = Tkinter.Tk()
root.withdraw()
#Options
ONE_FILE = "-F"

def Start():
    print ("Welcome to PyInstaller CLI interface %s by |Walen|\n") %  version
    print ("Feeling good... Now select a .py file wish you want to compile")
 #   os.system("pause")
    path_to_py = tkFileDialog.askopenfilename()

    if path_to_py == '':
        print ("You have not selected any .py file")
        print ("Script is shutting down!")
    #    os.system("pause")
        os.system('taskkill /f /im python.exe')

    if ".py" in path_to_py:
        print ("Well done!")
    else:
        print ("You select >WRONG< .py file")
        print ("Script is shutting down!")
    #    os.system("pause")
        os.system('taskkill /f /im python.exe')
    return path_to_py

def FirstStart():
    print ("Welcome to PyInstaller CLI interface %s by |Walen|\n") %  version
    print ("Select path to python.exe!")
    path_to_python = tkFileDialog.askopenfilename()

    if path_to_python == '':
        print ("You have not selected python.exe path")
        print ("Script is shutting down!")
     #   os.system("pause")
        os.system('taskkill /f /im python.exe')

    if "python.exe" in path_to_python:
        print ("Well done! I'm save your path to python.exe")
    else:
        print ("You have select >WRONG< python.exe path")
        print ("Script is shutting down!")
    #    os.system("pause")
        os.system('taskkill /f /im python.exe')

    print ("Select path to PyInstaller.py!")
    print ("Select Pyinstaller.py file\n")

   # os.system("pause")
    path_to_pyinstaller = tkFileDialog.askopenfilename()

    if path_to_pyinstaller == '':
        print ("You have not selected Pyinstaller.py path")
        print ("Script is shutting down!")
        os.system("pause")
        os.system('taskkill /f /im python.exe')

    if "pyinstaller.py" in path_to_pyinstaller:
        print ("Well done! I'm save your path to Pyinstaller.py")
    else:
        print ("You have select >WRONG< Pyinstaller.py path")
        print ("Script is shutting down!")
        os.system("pause")
        os.system('taskkill /f /im python.exe')

    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.add_section('Path_to_Pyinstaller')
    config.set('Path_to_Pyinstaller', (path_to_pyinstaller))
    config.add_section('Path_to_Python')
    config.set('Path_to_Python', (path_to_python))
    with open('settings.ini', 'wb') as configfile:
        config.write(configfile)
    return path_to_pyinstaller, path_to_python


try:
    settings = open("settings.ini", "r").read()
    path_to_pyinstaller = str(settings).split("]") [1].split("=") [0].replace(' ', '')
    final_pass_to_path_to_pyinstaller = str(path_to_pyinstaller.split("/") [-1])
    path_to_python = str(settings).split("]") [2].split("=") [0].replace(' ', '')
    if final_pass_to_path_to_pyinstaller in path_to_pyinstaller:
        path_to_py = Start()
        pass
except:
    path_to_pyinstaller, path_to_python = FirstStart()


if final_pass_to_path_to_pyinstaller in path_to_pyinstaller:
    path_to_pyinstaller = path_to_pyinstaller.split("\n") [1]
    path_to_python = path_to_python.split("\n") [1]
else:
    path_to_py = Start()

print ("""\nYour path to PyInstaller is |%s|
Your path to .py is |%s|""") % (path_to_pyinstaller, path_to_py)

print  ("\nLet's start!")
print ("Select one option and press ENTER\n")

print path_to_pyinstaller
print path_to_python


choise = int(input("""1. Compile with NO options <standard compile> :
2. Compile with -F <ONE FILE> option. Create a single file deployment : \n"""))
if choise == 1:
    compile = subprocess.Popen("%s %s %s" % (path_to_python, path_to_pyinstaller, path_to_py), shell=True).communicate()
    print ("It works! Well done %username%! Your .exe file is in <dist> folder! kk")
if choise == 2:
    compile = subprocess.Popen("%s %s %s %s" % (path_to_python, path_to_pyinstaller, path_to_py, ONE_FILE), shell=True).communicate()
    print ("It works! Well done %username%! Your .exe file is in <dist> folder! kk")



