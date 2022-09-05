from io import BytesIO
from gtts import gTTS
from pygame import mixer
import time

mixer.init() #Initialzing pyamge mixer

class SpeechController:
    """ This class handles the speech output to give an auditive feedback to the user's input. """

    def say(self, text, lang="en"):
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        mixer.music.load(mp3_fp,"mp3")  # Loading Music File
        mixer.music.play()  # Playing Music with Pygame

    def kill_proc(self):
        # nothing to do
        mixer.music.stop()
        pass

if __name__ == '__main__':
    speech_controller = SpeechController()
    speech_controller.say(
        "I am very hungry, what about lunch? This is a very long text. I would like to eat something fancy!!")
    time.sleep(3)
    speech_controller.say("Das ist ein deutscher Text", "de")

    time.sleep(2)
    print("After sleep, stopping sound")
    speech_controller.kill_proc()