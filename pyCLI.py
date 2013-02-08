#-*- coding:utf-8 -*-
__author__ = "lwalenl aka GreenUA"

import os
import subprocess
import Tkinter, tkFileDialog


version = "v.0.01 - *trunk*-chanel"
root = Tkinter.Tk()
root.withdraw()

def Start():
    print ("Welcome to PyInstaller CLI interface %s by |Walen|\n") %  version
    print ("Feeling good... Now choose a .py file wish you want to compile")
    os.system("pause")
    path_to_py = tkFileDialog.askopenfilename()

    if path_to_py == '':
        print ("You have not selected any .py file")
        print ("Script is shutting down!")
        os.system("pause")
        os.system('taskkill /f /im python.exe')

    if ".py" in path_to_py:
        print ("Well done!")
    else:
        print ("You select >WRONG< .py file")
        print ("Script is shutting down!")
        os.system("pause")
        os.system('taskkill /f /im python.exe')
    return path_to_py

def FirstStart():
    print ("Welcome to PyInstaller CLI interface %s by |Walen|\n") %  version
    print ("Select path to PyInstaller.py!")
    print ("----------------------------------")
    print (" AFTER THAT PLEASE RESTART SCRIPT")
    print ("----------------------------------")
    print ("Select Pyinstaller.py file\n")
    os.system("pause")
    file_path = tkFileDialog.askopenfilename()
    path_to_pyinstaller = file_path

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
    config.add_section('Path')
    config.set('Path', (file_path))
    with open('settings.ini', 'wb') as configfile:
        config.write(configfile)
    return path_to_pyinstaller

try:
    settings = open("settings.ini", "r").read()
    path_to_pyinstaller = str(settings).split("]") [1].split("=") [0].replace(' ', '')
    final_pass_to_path_to_pyinstaller = str(path_to_pyinstaller.split("/") [-1])
    if final_pass_to_path_to_pyinstaller in path_to_pyinstaller:
        path_to_py = Start()
        pass
except:
    path_to_pyinstaller = FirstStart()

path_to_pyinstaller = path_to_pyinstaller.split("\n") [1]
print ("""\nYour path to PyInstaller is |%s|
Your path to .py is |%s|""") % (path_to_pyinstaller, path_to_py)
print  ("\nLet's start!")
print ("Select one option and press ETNER\n")


choise = int(input("1. Compile with NO options <standard compile> : "))
if choise == 1:
    compile = subprocess.Popen("%s %s" % (path_to_pyinstaller, path_to_py), shell=True).communicate()
    print ("It works! Well done %username%! Your .exe file is in <build> folder! kk")



