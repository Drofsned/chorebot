import os
import sys
import random
import config

def main():
        text = ""
        while text != config.GOODBYE_MESSAGE:
                text = get_text(raw_input(config.PROMPT))
                os.system(get_output(text))

def get_output(txt):
        voice=get_rand_voice()
        dump_errors = " 2>/dev/null" if sys.platform == 'linux2' else ""
        return 'espeak -a {} -s {} -v {} "{}"{}'.format(config.AMPLITUDE, config.SPEED, voice, txt, dump_errors)

def get_rand_voice():
        return config.LANG+random.choice(config.MALES)

def get_text(txt):
        txt = config.GOODBYE_MESSAGE if txt.lower() in config.EXIT_LIST else txt
        return config.NO_TEXT_MESSAGE if not txt else txt

if __name__== "__main__":
        main()