# This only exists so my main file doesnt have this massive blob of text in the middle

help_reply = """**!split <Runescape name>: Gets the splits for the given user**
e.g. !split Jagax 
"""

admin_help_reply = """These commands are for admins only:

**!update <Runescape name>, <amount>, <list of items>:**
Adds <amount> to the player's split (accepts negative numbers). *Do NOT add commas in the number or you'll break everything*. 
e.g. !update Jagex, 500000
e.g. !update Jagex, 17000, Theatre of Blood Cabbages x500

**!add_user <Runescape name>, <splits>, <join date>, <items>:**
Creates the user if that name doesnt already exist. You can also set their starting split, join date, and items. While these last three are optional, they must be added in that order (e.g. if you have a date but no starting split value, you must enter 0 for splits).
If no join date is added, it defaults to today's date. Dates must also be of the form MM/DD/YYYY. 
examples: 
!add_user Jagex2
!add_user Jagex2, 500000, 5/20/2019, Ancestral Robe Top, Dexterous Prayer Scroll
!add_user Jagex2, 0, 1/30/2019
"""

API_error = """API Error! There's been too many commands in too short of a period of time. The API can only handle 100 actions per 100 seconds. 
Please wait at least two minutes and try again"""

Initial_Message = "If any of these values are incorrect, please modify or delete the congifs.json file located in the Configs folder, and restart the bot"