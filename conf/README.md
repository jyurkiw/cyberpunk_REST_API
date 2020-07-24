# Setup

There is no setup script so you'll have to do some setup yourself.

Step 1: Install Apache2

Step 2: Install MongoDB-Community

Step 3: Install Python3, Pip, and virtualenv

Step 4: Download the CP2020_Discord_Bot_API project from github:

- git clone <https://github.com/jyurkiw/CP2020-Discord-Bot-API.git>

Step 5: Point WSGI at the CP2020_Discord_Bot_API.

- vim path/to/cyberpunkapp.wsgi
- Change [path-to-CP2020_Discord_Bot_API module] to point to wherever you cloned the CP2020_Discord_Bot_API repo. Check Step 5 by:

  ```
    python3
    >> import sys
    >> sys.path.insert(1, "[path-to-CP2020_Discord_Bot_API module]")
    >> import CP2020_Discord_Bot_API
  ```

- If python tells you it can't find it you're not done step 5 yet.

- NOTE: The path should be pointing to the directory **above** the module since a CP2020_Discord_Bot_API/**init**.py file exists.

Step 6: Put your server address and admin email into the sites-available/CyberpunkApp.conf file.

Step 7: Put CyberpunkApp.conf and cyberpunkapp.wsgi into their proper locations.

- **THIS STEP IS SERVER-DEPENDENT**.
- You may need to google a few things.
- CyberpunkApp.conf goes into /etc/apache2/sites-available on Ubuntu 18.04.4 LTS
- cyberpunk.wsgi goes into /var/www/CyberpunkApp on Ubuntu 18.04.4 LTS

Step 8: Turn on Apache and MongoDB.

- Google!
