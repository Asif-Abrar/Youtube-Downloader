from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError
from pytube.exceptions import MembersOnly
from pytube.exceptions import RecordingUnavailable
from pytube.exceptions import VideoUnavailable
from pytube.exceptions import VideoPrivate
from pytube.exceptions import VideoRegionBlocked
import pathlib
import time
import logging

# Download path in local directory
path = "H:/Mixed_Album_mp3/"

# --------------Logger Settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create file handler which logs even info messages
fh = logging.FileHandler('INFO.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


# -----Timed Decorator
def timed(function):
    def wrapper():
        before = time.time()
        value = function()
        after = time.time()
        function_name = function.__name__
        print(f"{function_name} took {after - before} seconds to execute!")
        logger.info(f"{function_name} took {after - before} seconds to execute!")
        return value
    return wrapper


def choice_1():
    print("Executing choice 1...")
    logger.info("Executing choice 1...")
    url = input("Enter the url: ")
    logger.info(url)

    try:
        yt = YouTube(url)
        selected = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        logger.info(selected)
        file = pathlib.Path(path + selected.default_filename)

        if file.exists():
            print(f"{selected.default_filename} is already downloaded!")
            logger.info(f"{selected.default_filename} is already downloaded!")
        else:
            yt.streams.filter(progressive=True).order_by('resolution') \
                .desc().first().download(output_path=path)
            print(f"{selected.default_filename} downloaded!")
            logger.info(f"{selected.default_filename} downloaded!")

    except RegexMatchError as e:
        logger.error(e)
    except MembersOnly as e:
        logger.error(e)
    except RecordingUnavailable as e:
        logger.error(e)
    except VideoPrivate as e:
        logger.error(e)
    except VideoRegionBlocked as e:
        logger.error(e)
    except VideoUnavailable as e:
        logger.error(e)


def choice_2():
    print("Executing choice 2...")
    logger.info("Executing choice 2...")
    url = input("Enter the url: ")
    logger.info(url)
    count = 0

    try:
        pl = Playlist(url)

        for video in pl.videos:
            selected = video.streams.filter(progressive=True, file_extension='mp4') \
                .order_by('resolution').desc().first()
            logger.info(selected)
            file = pathlib.Path(path + selected.default_filename)

            if file.exists():
                print(f"{selected.default_filename} is already downloaded!")
                logger.info(f"{selected.default_filename} is already downloaded!")
            else:
                video.streams.filter(progressive=True, file_extension='mp4') \
                    .order_by('resolution').desc().first().download(output_path=path)
                count += 1
                print(f"{count}. {selected.default_filename} downloaded!")
                logger.info(f"{count}. {selected.default_filename} downloaded!")

        print(f"Total {count} files downloaded successfully!")
        logger.info(f"Total {count} files downloaded successfully!")

    except RegexMatchError as e:
        logger.error(e)
    except MembersOnly as e:
        logger.error(e)
    except RecordingUnavailable as e:
        logger.error(e)
    except VideoPrivate as e:
        logger.error(e)
    except VideoRegionBlocked as e:
        logger.error(e)
    except VideoUnavailable as e:
        logger.error(e)


def choice_3():
    print("Executing choice 3...")
    logger.info("Executing choice 3...")
    url = input("Enter the url: ")
    logger.info(url)

    try:
        yt = YouTube(url)
        yt.check_availability()
        selected = yt.streams.filter(only_audio=True).first()
        logger.info(selected)
        file = pathlib.Path(path + selected.default_filename)

        if file.exists():
            print(f"{selected.default_filename} is already downloaded!")
            logger.info(f"{selected.default_filename} is already downloaded!")
        else:
            yt.streams.filter(only_audio=True).first().download(output_path=path)
            print(f"{selected.default_filename} downloaded!")
            logger.info(f"{selected.default_filename} downloaded!")

    except RegexMatchError as e:
        logger.error(e)
    except MembersOnly as e:
        logger.error(e)
    except RecordingUnavailable as e:
        logger.error(e)
    except VideoPrivate as e:
        logger.error(e)
    except VideoRegionBlocked as e:
        logger.error(e)
    except VideoUnavailable as e:
        logger.error(e)


def choice_4():
    print("Executing choice 4...")
    logger.info("Executing choice 4...")
    url = input("Enter the url: ")
    logger.info(url)
    count = 0

    try:
        pl = Playlist(url)

        for video in pl.videos:
            selected = video.streams.filter(only_audio=True).first()
            logger.info(selected)
            file = pathlib.Path(path + selected.default_filename)
            if file.exists():
                print(f"{selected.default_filename} is already downloaded!")
                logger.info(f"{selected.default_filename} is already downloaded!")
            else:
                video.streams.filter(only_audio=True).first().download(output_path=path)
                count += 1
                print(f"{count}. {selected.default_filename} downloaded!")
                logger.info(f"{count}. {selected.default_filename} downloaded!")

        print(f"Total {count} files downloaded successfully!")
        logger.info(f"Total {count} files downloaded successfully!")

    except RegexMatchError as e:
        logger.error(e)
    except MembersOnly as e:
        logger.error(e)
    except RecordingUnavailable as e:
        logger.error(e)
    except VideoPrivate as e:
        logger.error(e)
    except VideoRegionBlocked as e:
        logger.error(e)
    except VideoUnavailable as e:
        logger.error(e)


def y_downloader():
    while True:
        choice = str(input('''
    Press "1" for video/mp4,
    Press "2" for playlist,
    Press "3" for mp3,
    Press "4" for playlist as mp3 or
    Press "q" to Quit: '''))

        if choice == "1":
            choice1 = timed(choice_1)
            choice1()
        elif choice == "2":
            choice2 = timed(choice_2)
            choice2()
        elif choice == "3":
            choice3 = timed(choice_3)
            choice3()
        elif choice == "4":
            choice4 = timed(choice_4)
            choice4()
        elif choice == "q":
            break
        else:
            logger.error("Wrong Input!")
            time.sleep(1)


y_downloader()
