bridgebot
=========

a simple IRC bot built on Python IRCUtils. originated 2011-03-10 to ease a network transitions for some friends. re-used 2012-08-02 for a different network transition.

this has been changed to use ConfigParser instead of hard-coded configs.

TODO:
* improve the config parsing
* add some CLI args (like --config)
* support more than 2 bots?
* improve the .join() logic
* investigate reconnect logic (reconnect+IRCUtils always kills me)
