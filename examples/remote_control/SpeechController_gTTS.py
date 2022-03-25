import asyncio

from gtts import gTTS
from io import BytesIO
from playsound import playsound
from io import BytesIO

from gtts import gTTS
from playsound import playsound
from tempfile import NamedTemporaryFile
import concurrent.futures

class SpeechController:
    """ This class handles the speech output to give an auditive feedback to the user's input. """

    def say(self, text, lang="en"):
#        mp3_fp = BytesIO()
#        tts = gTTS('hello', lang='en')
#        tts.write_to_fp(mp3_fp)
#        playsound()
        self.synthandspeak(text,lang)

    def synthandspeak(self, text, lang="en"):
        print("in synthandspeak")
        gTTS(text=text, lang=lang).write_to_fp(voice := NamedTemporaryFile())
        playsound(voice.name, False)
        voice.close()

    def kill_proc(self):
        # nothing to do
        pass

#speech_controller=SpeechController()
#speech_controller.say("This is an English text")
#speech_controller.say("Das ist ein deutscher Text","de")