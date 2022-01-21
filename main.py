import art
import os
from pytube import YouTube
from pytube.cli import on_progress
from tkinter.filedialog import askdirectory, askopenfilename


def automode():
    """ Check for 'yvd.txt' in the directory and start downloading"""
    def hello_auto_msg():
        """ Print a hello message"""
        print("                                            \u00a9 Ant.Butkov")
        print(art.text2art("YVD", "block"))
        print(art.text2art("Auto Mode"))

    links = []
    while True:
        with open("yvd.txt", 'r') as f:
            lines = f.readlines()
            if not lines:
                raise FileNotFoundError
            else:
                for line in lines:
                    links.append(line)
        break
    hello_auto_msg()
    for link in links:
        vid = YouTube(link)
        vid.streams.filter(file_extension='mp4').get_highest_resolution().download(
            output_path=os.getcwd())


def hello_msg():
    """ Print a hello message"""
    print("                                            \u00a9 Ant.Butkov")
    print(art.text2art("YVD", "block"))
    print("         Welcome to YoutubeVideoDownloader \nTo download, enter the URL of the desired video "
          "below \n         Type 'FILE' to load URL from file \n        (Each URL must start on a new line) \n "
          "          Type 'GO' to start downloading \n          Then select the folder to save"
          " \n      To cancel file download press 'Ctrl+C'")


def get_url():
    """ Get video URL`s from file or user input """
    links = []
    while True:
        url = input("Enter the URL: \n -> ")
        if url.lower() == "go":
            break
        elif url.lower() == "file":
            try:
                url_file = askopenfilename()
                print('   \u21b3 {}' .format(url_file))
                with open(url_file, 'r') as f:
                    lines = f.readlines()
                    if not lines:
                        raise ValueError
                    else:
                        for line in lines:
                            links.append(line)
                    break
            except ValueError:
                print('     \u21b3 Error loading URL from file ')
        else:
            links.append(url)
    return links


def download(url, path):
    """ Start downloading video files """
    vid = YouTube(url, on_progress_callback=on_progress)
    print("\n {}.mp4".format(vid.title))
    try:
        vid.streams.filter(file_extension='mp4').get_highest_resolution().download(
            output_path=path)
    except Exception:
        print(" \n   \u21b3 Downloading error")
    except KeyboardInterrupt:
        print("\n    \u21b3 Canceled by user")


def win_exit():
    """ Exit message for windows users """
    if os.name == 'nt':
        import msvcrt
        print('\n              ----Press any key for exit----')
        msvcrt.getch()


def main():
    """ Run a program"""
    try:
        automode()
    except FileNotFoundError:
        try:
            hello_msg()
            links = get_url()
            dst = askdirectory()
            print('                     ---Downloading---')
        except KeyboardInterrupt:
            exit()
        for link in links:
            try:
                download(link, dst)
            except Exception:
                print('\n {} \n \u21b3 Connection error' .format(link))
                pass
    win_exit()


if __name__ == '__main__':
    main()
# (c)Ant.Butkov
