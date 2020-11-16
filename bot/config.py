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
# sequence to put before an import
# es: "#:>imp-time" is valid if the IMPCHRSEQ is "#:>" and "imp-time" is in the IMPORTS_MAP
# this IMP_TOKEN is supposed to have a # as first charachter because if the preprocessor doesn't
# find a corrispondency will leave the #:>imp-somehthing as is
IMP_TOKEN = "#:>"
# avabile imports via preprocessor
IMPORTS_MAP = {
    "imp-time": "import time",
    "imp-time-func": "from time import time",
    # difflib has a function aboout files but not this from
    "imp-sequencematcher-obj": "from difflib import SequenceMatcher",
    "imp-get_close_matches-func": "from difflib import get_close_matches"  # the same for this
    "imp-pprint": "import pprint",
    "imp-pprint-func": "from pprint import pprint",
    "imp-random": "import random",
    "imp-os": "print('lol we are not so dumb bro, you CANT import os')",
    "imp-struct": "import struct",
    "imp-string": "import string",
    "imp-math": "import math",
    "imp-this": "import this",
    "imp-antigravity": "print('https://xkcd.com/353/')"
}
