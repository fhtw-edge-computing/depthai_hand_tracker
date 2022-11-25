import subprocess
import time

langMapping = {
    "de": "de-DE",
    "en": "en-US"
}

class SpeechController:
    """ This class handles the speech output to give an auditive feedback to the user's input. """
    speakHandler = None
    currentLang = "de"

    def say(self, text, lang="en"):
        self.kill_proc()
        print(f'speaking text: {text}')
        self.setLang(lang)
        subprocess.run(['pico2wave', f'--lang={langMapping.get(self.currentLang)}', '-w', '/tmp/pico.wav', f'"{text}"'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        self.speakHandler = subprocess.Popen(['aplay', '/tmp/pico.wav'])

    def kill_proc(self):
        if self.speakHandler:
            self.speakHandler.terminate()
        subprocess.run(['rm', '-f', '/tmp/pico.wav'])
        self.speakHandler = None

    def setLang(self, lang):
        self.currentLang = lang


if __name__ == '__main__':
    speech_controller = SpeechController()
    speech_controller.say(
        "I am very hungry, what about lunch? This is a very long text. I would like to eat something fancy!!","en")
    time.sleep(3)
    speech_controller.say("Das ist ein deutscher Text", "de")

    time.sleep(2)
    print("After sleep, stopping sound")
    speech_controller.kill_proc()