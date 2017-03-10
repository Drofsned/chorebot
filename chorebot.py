import os
import sys
import random

AMPLITUDE = 300
SPEED = 100
LANG = "english-us"
MALES = ["+m"+str(i) for i in range(1,8)]
FEMALES = ["+f"+str(i) for i in range(1,5)]
EXIT_LIST = ["bye", "bye bye", "later", "goodbye", "so long"]

def main():
        text = "Clean your room..."
        loop = True

        while loop:
                text = raw_input('Say: ')
                if text == "":
                        text = "You didn't type anything for me to say. What are you thinking?"
                if text in EXIT_LIST:
                        text = "Later broh!"
                        loop = False
                os.system(generate_output(text))

def generate_output(txt):
        voice=get_rand_voice()
        dump_errors = " 2>/dev/null" if sys.platform == 'linux2' else ""
        #return 'espeak -a {} -s {} -v {} "{}" 2>/dev/null'.format(AMPLITUDE, SPEED, voice, txt)
        return 'espeak -a {} -s {} -v {} "{}"{}'.format(AMPLITUDE, SPEED, voice, txt, dump_errors)

def get_rand_voice():
        return LANG+random.choice(MALES)

if __name__== "__main__":
        main()
