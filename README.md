# YVD
Simple YouTube Video Downloader

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django?logo=python)![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Cyero/YVD?include_prereleases&label=v1.0&logo=windows)

###   1. Installation and run


***If you have downloaded the release version for windows - go to the section "Usage"***

Open the terminal in the directory with the program files. if you are using pip run the following code:
```
pip install -r requirements.txt
```
if you are using poetry run the following code:
```
poetry install
```
After the necessary dependencies are installed, you can run the program executable file "main.py" (run "main_ru.py" if you want to run the program with Russian interface)


### 2. Usage 


After launch, the program will automatically check for the presence of the "yvd.txt" file in the directory with the program's executable file. If this file is found, the automatic mode will start, and all files will be loaded into the directory with the program files. 

If the "yvd.txt" file was not in the directory, the main window of the program will open in front of you, in which you will be asked to enter the url of the video you need to download. You can enter as many urls as you need. After entering all the necessary url to start the video download process, you must enter "GO" in the URL input field. (If you enter "FILE" in the URL field you will be prompted to open a file containing the necessary links to download. This type of download works well if you need to download a large number of videos). 

In the next dialog box you will be asked to specify a directory to save the video. Sometimes the directory selection window may open behind the main program window, so if you do not see it, just move the main program window to another area of the screen. 

The download process has begun, you will be informed about its results in the main program window. If you need to cancel the download of the current file, press the key combination "Ctrl + C"


### 3. URL file requirements


As for the "yvd.txt" file, as well as for any other files containing links to videos, there is only one rule - each link must start on a new line in the file.

