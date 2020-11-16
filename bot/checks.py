def check_long_message(text):
    text = str(text)
    if not text:
        return 'This should not happen'
    if len(text) > 2000:
        return text[:2000] + '... truncated <too long message>'
    else:
        return text
