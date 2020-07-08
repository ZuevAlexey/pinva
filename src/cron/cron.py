from bot import bot
from time import sleep


def run():
    while True:
        run_daily_report()
        sleep(1)


def run_daily_report():
    bot.send_message(82374, 'hello')
