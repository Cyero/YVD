import art
import os
from pytube import YouTube
from pytube.cli import on_progress
from tkinter.filedialog import askdirectory, askopenfilename


def automode():
    """ Check for 'yvd.txt' in the directory"""
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
    print("         Добро пожаловать в YoutubeVideoDownloader \n       Для загрузки укажите URL желаемых видео "
          "ниже \n         Введите 'FILE' для загрузки URL из файла \n      (Каждый URL должен начинаться с "
          "новой строки) \n            Введите 'GO' чтобы начать загрузку \n         После чего укажите папку "
          "для сохранения \n       Для отмены загрузки файла нажмите 'Ctrl+C'")
        

def get_url():
    """ Get video URL`s from file or user input """
    links = []
    while True:
        url = input("Введите URL видео: \n -> ")
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
                print('     \u21b3 Ошибка загрузки URL из файла')
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
        print(" \n   \u21b3 Ошибка загрузки")
    except KeyboardInterrupt:
        print("\n    \u21b3 Отменено пользователем")


def win_exit():
    """ Exit message for windows users """
    if os.name == 'nt':
        import msvcrt
        print('\n         ---- Для выхода нажмите любую клавишу ----')
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
            print('                     --- Загружается ---')
        except KeyboardInterrupt:
            exit()
        for link in links:
            try:
                download(link, dst)
            except Exception:
                print('\n {} \n \u21b3 Ошибка подключения' .format(link))
                pass
    win_exit()


if __name__ == '__main__':
    main()
