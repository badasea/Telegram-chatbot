from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,)
import logging
from bs4 import BeautifulSoup
import requests
import urllib.request

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
token = '995431944:AAGtk6itESHU_z-IrS2Ppv0PCKk3H9ynjIo'


def Hello(bot, updata):
    bot.send_message(chat_id=updata.message.chat_id, text="안녕하세요 ")

def Naver_moive_ranklist(self, update):
    session = requests.Session()
    addr = 'http://movie.naver.com/movie/running/current.nhn'

    self.addr = addr
    req = session.get(self.addr)
    soup = BeautifulSoup(req.text, "html.parser")
    titles = soup.find_all('dl', class_='lst_dsc')

    rank = 1
    for title in titles:
        update.message.reply_text(str(rank) + '위: ' + title.find('a').text + "\n"
                                  + "Link : " + addr + title.find('a')['href'] + "\n"
                                  )

        rank += 1
        if (rank == 11):
            break

def main() :
    updater = Updater(token)
    dp = updater.dispatcher
    print("Bot started")

    updater.start_polling()
    dp.add_handler(CommandHandler('hello', Hello))
    dp.add_handler(CommandHandler('movierank', Naver_moive_ranklist))

    updater.idle()
    updater.stop()

if __name__ == '__main__':
    main()




