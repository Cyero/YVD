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
    except Exception:
        print("                                            \u00a9 Ant.Butkov")
        print(art.text2art("YVD", "block"))
        print("         Добро пожаловать в YoutubeVideoDownloader \n       Для загрузки укажите URL желаемых видео "
              "ниже \n         Введите 'FILE' для загрузки URL из файла \n      (Каждый URL должен начинаться с "
              "новой строки) \n            Введите 'GO' чтобы начать загрузку \n         После чего укажите папку "
              "для сохранения \n       Для отмены загрузки файла нажмите 'Ctrl+C'")
        links = []
        while True:
            url = input("Введите URL видео: \n -> ")
            if url.lower() == "go":
                dst = askdirectory()
                print('                     ---Загружается---')
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
                    print('                     ---Загружается---')
                    break
                except Exception:
                    print('     \u21b3 Ошибка загрузки URL из файла')
            else:
                links.append(url)
        for link in links:
            try:
                vid = YouTube(link, on_progress_callback=on_progress)
                print("\n {}.mp4".format(vid.title))
                try:
                    vid.streams.filter(file_extension='mp4').get_highest_resolution().download(output_path=dst)
                except Exception:
                    print(" \n   \u21b3 Ошибка загрузки")
            except Exception:
                print('\n {} \n \u21b3 Ошибка подключения' .format(link))
                pass


if __name__ == '__main__':
    download()
# (c)Ant.Butkov
