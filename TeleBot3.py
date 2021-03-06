import time
import sys
import random
import datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from blink1.blink1 import Blink1

try:
    blink1 = Blink1()
except:
    print("no blink1 found")
    sys.exit()

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#led = 16

#GPIO.setup(led, GPIO.OUT)

#def LedOn(val):
#    GPIO.output(led,1)
#    time.sleep(val)
#    GPIO.output(led,0)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/On':
        #bot.sendMessage(chat_id, random.randint(1,6))
        #LedOn(5)
        blink1.fade_to_rgb(1000, 255, 255, 255)
    elif command == '/Off':
        blink1.fade_to_rgb(1000, 0, 0, 0)
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
time.sleep(10)
