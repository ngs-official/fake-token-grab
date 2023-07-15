# Discord Fake Token Grabber
Fake Discord token grabber that is, like my other projects, free and open source for anyone to use. ![image](https://github.com/ngs-official/fake-token-grab/assets/123272327/c2d1ceb3-0544-424a-81b1-7d90fb9d5832) <br /> (Don't waste your time trying to get the token from this image, it's fake)


**Requirements:**
* Python with standard libaries (https://www.python.org/downloads/)
* Discord.py (https://pypi.org/project/discord.py/)

**Download:**
Download the 'config.txt' file, the 'start.bat' file, and finally the 'tokenGrabber.py' file

**How to use:**
1. Put your bot's token in the first line of the 'config.txt' file and then your preferred prefix in the second (Don't know how? Look at the 'Other' section below)
2. Open the 'start.bat' file to start up the bot
3. Turn on developer mode in settings under the 'Advanced' category
4. Get the user ID of your target (search up how)
5. Use the command '!grab [userID]' in a server with the bot added and the bot will send you an embed with a fake token amongst other things* 

**Other:**
1. To make a bot, go to https://discord.com/developers/applications and create an application
2. After creating a new application, click on the 'Bot' category in the bar on the left
3. Scroll down and enable all the privilegied gateway intents, which are the last three toggles (presence intent, server members intent, and message content intent)
4. Scroll back up and click on 'Reset Token' to get your bot's token
5. You now have a working bot, and you can put the token in the 'config.txt' file as mentioned in the 'How to use' section, then continue to follow everything there

**More:** <br />
* You can contact me on Discord and Telegram at J0HAN#6805 and @johan_real respectively
* How does this work? Well basically the start of a user's Discord token is their user ID in Base64, and the rest of the token is just randomly generated. When users check their token they will see that it starts the same as the token you 'grabbed' and will get creeped out (as I highly doubt they'll look at the whole thing)
* Oh yeah make sure all the files are in one folder with no other files in it
* Probably won't update this, my main project will be 'JOHAN NUKER' (https://github.com/ngs-official/johan-nuker) <br />

*Your prefix may not be '!', instead use whatever prefix you put in the 'config.txt' file's second line
