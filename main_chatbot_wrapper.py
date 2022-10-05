def main():
    updater=Updater(TOKEN,use_context=True)
    disp=updater.dispatcher
    disp.add_handler(CommandHandler("start",start))
    #disp.add_handler(MessageHandler(Filters.text,grapher))
    disp.add_handler(MessageHandler(Filters.text,text_msg))
    #disp.add_handler(MessageHandler(Filters.photo,photo))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()