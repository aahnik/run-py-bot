'''
Configs for the bot
'''

# expressions which are banned
BANNED = ['quit', 'input', 'open', 'import', 'exit', 'exec']

# timeout in seconds
TIMEOUT = 6

TIMEOUT_MESSAGE = f'''😢 Timeout of {TIMEOUT} reached.
I have limited resources. 
You may increase the timeout and run this bot on your own server if required.'''

RESTRICT_MESSAGE = f'☹️ SECURITY ISSUE:\nYou have used a restricted word \n{BANNED}'
