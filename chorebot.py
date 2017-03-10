import os
import sys
import random
import config

def main(loop):
        while loop:
                text = raw_input(config.PROMPT)
                text = config.NO_TEXT_MESSAGE if not text else text
                if text.lower() in config.EXIT_LIST:
                        text = config.GOODBYE_MESSAGE 
                        loop = False
                os.system(generate_output(text))

def generate_output(txt):
        voice=get_rand_voice()
        dump_errors = " 2>/dev/null" if sys.platform == 'linux2' else ""
        return 'espeak -a {} -s {} -v {} "{}"{}'.format(config.AMPLITUDE, config.SPEED, voice, txt, dump_errors)

def get_rand_voice():
        return config.LANG+random.choice(config.MALES)

if __name__== "__main__":
        main(True)
