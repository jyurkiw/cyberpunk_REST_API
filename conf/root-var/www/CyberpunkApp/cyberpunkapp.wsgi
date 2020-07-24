#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/CyberpunkApp/")
sys.path.insert(1, "[path-to-CP2020_Discord_Bot_API module]")

from CyberpunkApp import createApp

application = createApp()
application.secret_key = "[SECRET_KEY_HERE]"
