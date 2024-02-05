import getpass
import os
import shutil

from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def url_to_mp3(video_url: str):
    try:
        # Download the audio-only stream
        video = YouTube(video_url)
        video.check_availability()

        # Prompt user to log in if the video is age-restricted
        if video.age_restricted:
            print(
                "This video is age-restricted. Please log in to your YouTube account."
            )
            username = input("YouTube Username: ")
            password = getpass.getpass("YouTube Password: ")

            video.login(username, password)
            print("Logged in successfully.")

        video_file = video.streams.filter(only_audio=True).first()
        print("Downloading...")
        video_file.download()

        # Rename and move the downloaded file to the "audio" directory
        mp4_name = video_file.default_filename
        mp3_name = mp4_name.replace(".mp4", ".mp3")
        os.rename(mp4_name, mp3_name)

        if not os.path.exists("audio"):
            os.makedirs("audio")

        shutil.move(mp3_name, os.path.join("audio", mp3_name))
        print("Conversion completed!")

    except VideoUnavailable:
        print("Video is not available.")

    except Exception as e:
        print(f"Something went wrong: {e}")


def main():
    try:
        input_url = input("Please enter a URL: ")
        url_to_mp3(video_url=input_url)
    except KeyboardInterrupt:
        print("\nDownload canceled by user.")
    finally:
        print("Exiting...")


if __name__ == "__main__":
    main()
