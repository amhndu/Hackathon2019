import itertools
import re
import datefinder
import api

_redact_patterns = (re.compile(pattern, re.I) for pattern in (
        r'\b\d{6}\d*\b', # long number
        r'\b([+]?\d{1,2})?(\d{3}?){2}\d{4}\b', # mobile number
        r'\b[A-Za-z]{5}\d{4}[A-Za-z]{1}\b', # pan
        r'\b\d{4}\s\d{4}\s\d{4}\b', # aadhar
        r'\bmale|female\b', # gender
    ))

_sensitive_entities = (
        'Name',
        'Person',
        'IPAddress',
        'Location',
        'EmailAddress',
        'Company',
        'Organization'
    )

def redact(text):
    placeholder = 'XXXX'
    redacted_text = text

    entities = api.processResponse(api.sendRequest(text))
    
    for entity in entities:
        if entity['type'] in _sensitive_entities:
            redacted_text = redacted_text.replace(entity['text'], placeholder)

    for pattern in _redact_patterns:
        redacted_text = re.sub(pattern, placeholder, redacted_text)

    for _, date_string in datefinder.find_dates(redacted_text, source=True):
        print(date_string)
        if date_string[:3] in ('on ', 'at '):
            date_string = date_string[3:]
        redacted_text = redacted_text.replace(date_string, placeholder)

    return redacted_text
