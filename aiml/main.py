#!/usr/bin/python
# -*- coding: utf-8 -*-

import aiml
bot=aiml.Kernel()
bot.learn("base.xml")
while True: print bot.respond(raw_input("User> "))

