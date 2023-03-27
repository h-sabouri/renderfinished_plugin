import nuke2
import PySide2.QtMultimedia
import os

show_notification = True

play_sound = True

sound_file = "{}/magic.wav".format(os.path.dirname(__file__))


def notify_user():
    if show_notification:
        nuke.message("Render Finished")

    if play_sound:
        PySide2.QtMultimedia.QSound.play(sound_file)