#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/CyberpunkApp/")
sys.path.insert(1, "/home/ubuntu/pylibs")

from CyberpunkApp import createApp

application = createApp()
application.secret_key = "[SECRET_KEY_HERE]"
