#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from bot import start_bot

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start_bot(bot_token=sys.argv[1])
    else:
        print "Running: python start_bot.py you_bot_token"
