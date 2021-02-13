import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

LOG_PATH = settings.LOG_PATH
logging.basicConfig(filename=LOG_PATH, level=logging.INFO)


def _greet_user(update, context):
    """
    Greeting user function
    :param update: update object
    :param context: context
    :return:
    """
    logging.info('User pressed start')
    update.message.reply_text('Hello, user! You started messaging')


def _talk_to_me(update, context):
    """
    Echo function
    :param update: update object
    :param context: context
    :return:
    """
    user_text = update.message.text
    logging.info(f'User was echoed with {user_text}')
    update.message.reply_text(user_text)


def main():
    """
    Main function
    :return:
    """
    bot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', _greet_user))
    dp.add_handler(MessageHandler(Filters.text, _talk_to_me))

    logging.info('Started')
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
