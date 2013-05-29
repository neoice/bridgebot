#!/usr/bin/python
from ircutils import bot, format, start_all

import os
import ConfigParser

cwd = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser.ConfigParser()
config.read(cwd + '/bridgebot.cfg')

class BridgeBot(bot.SimpleBot):
    def on_welcome(self, event):
        self.join( self.foobar )

    def on_message(self, event):
        msg = "<" + event.source + "> " + event.message
        self.friend.send_message(event.target, msg)

if __name__ == "__main__":
    bot1 = BridgeBot( config.get('network1', 'nick') )
    bot1.user = config.get('network1', 'nick')
    bot1.real_name = config.get('network1', 'name')
    bot1.connect( config.get('network1', 'network') )
    bot1.join( config.get('network1', 'channel') )

    bot2 = BridgeBot( config.get('network2', 'nick') )
    bot2.connect( config.get('network2', 'network') )
    bot2.join( config.get('network2', 'channel') )

    bot1.friend = bot2
    bot2.friend = bot1

    bot1.foobar = config.get('network1', 'channel')
    bot2.foobar = config.get('network2', 'channel')

    start_all()
