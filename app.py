import pygame
import time
from datetime import datetime, timedelta
import os

def calculate_start_time(beat_drop_time_ms):
    """
    Calculate when to start the audio file so that the beat drop aligns with the next hour.

    :param beat_drop_time_ms: Time of the beat drop in milliseconds (int)
    :return: Time to start the audio file in seconds (float)
    """
    now = datetime.now()
    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    time_until_next_hour = (next_hour - now).total_seconds()

    return time_until_next_hour - (beat_drop_time_ms / 1000.0)

def play_audio(file_path, start_delay):
    """
    Play the audio file with a delay to synchronize the beat drop.

    :param file_path: Path to the audio file (str)
    :param start_delay: Time to wait before starting the audio in seconds (float)
    """
    print(f"{start_delay:.3f} seconds until audio begins")
    time.sleep(max(0, start_delay))

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("playing audio!")

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Keep the program alive until the music finishes

def main():
    audio_file = input("enter the path to the audio file: ").strip()

    if not os.path.exists(audio_file):
        print("the specified audio file does not exist.")
        return

    try:
        beat_drop_time_ms = int(input("enter the time of the beat drop in milliseconds: ").strip())
    except ValueError:
        print("please enter a valid number for the beat drop time.")
        return

    start_delay = calculate_start_time(beat_drop_time_ms)

    if start_delay < 0:
        print("the beat drop time is too close to the next hour. Try a different audio file or beat drop time.")
        return

    play_audio(audio_file, start_delay)

if __name__ == "__main__":
    main()
