import art
import os
from pytube import YouTube
from pytube.cli import on_progress
from tkinter.filedialog import askdirectory, askopenfilename


def download():
    try:
        links = []
        while True:
            with open("yvd.txt", 'r') as f:
                lines = f.readlines()
                if not lines:
                    raise ValueError
                else:
                    for line in lines:
                        links.append(line)
            break
        print("                                            \u00a9 Ant.Butkov")
        print(art.text2art("YVD", "block"))
        print(art.text2art("Auto Mode"))
        for link in links:
            vid = YouTube(link)
            vid.streams.filter(file_extension='mp4').get_highest_resolution().download(output_path=os.getcwd())
    except:
        print("                                            \u00a9 Ant.Butkov")
        print(art.text2art("YVD", "block"))
        print("         Welcome to YoutubeVideoDownloader \nTo download, enter the URL of the desired video "
              "below \n         Type 'FILE' to load URL from file \n        (Each URL must start on a new line) \n "
              "          Type 'GO' to start downloading \n          Then select the folder to save"
            " \n      To cancel file download press 'Ctrl+C'")
        links = []
        while True:
            url = input("Enter the URL: \n -> ")
            if url.lower() == "go":
                dst = askdirectory()
                print('                     ---Downloading---')
                break
            elif url.lower() == "file":
                try:
                    url_file = askopenfilename()
                    dst = askdirectory()
                    print('   \u21b3 {}' .format(url_file))
                    with open(url_file, 'r') as f:
                        lines = f.readlines()
                        if not lines:
                            raise ValueError
                        else:
                            for line in lines:
                                links.append(line)
                    print('                     ---Downloading---')
                    break
                except:
                    print('     \u21b3 Error loading URL from file ')
            else:
                links.append(url)
        for link in links:
            try:
                vid = YouTube(link, on_progress_callback=on_progress)
                print("\n {}.mp4".format(vid.title))
                try:
                    vid.streams.filter(file_extension='mp4').get_highest_resolution().download(output_path=dst)
                except:
                    print(" \n   \u21b3 Downloading error")
            except:
                print('\n {} \n \u21b3 Connection error' .format(link))
                pass


if __name__ == '__main__':
    download()
# (c)Ant.Butkov
