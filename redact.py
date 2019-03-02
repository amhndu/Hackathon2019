import itertools
import re
import datefinder
import api
from operator import itemgetter

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

def _find_all(a_str, sub):
    start = 0
    length = len(sub)
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield (start, start + length)
        start += length

def redact(text):
    masked = text

    locations = []
    
    entities = api.processResponse(api.sendRequest(text))
    for entity in entities:
        if entity['type'] in _sensitive_entities:
            key = entity['type']
            locations.extend(_find_all(masked, key))
            # mask off matched characters to remove them from further search
            masked = masked.replace(key, '*' * len(key))
            # doing twice the work here, fix this later

    for pattern in _redact_patterns:
        locations.extend((m.start(), m.end()) for m in re.finditer(pattern, masked))
        # mask off matched characters to remove them from further search
        masked = re.sub(pattern, lambda match: '*' * len(match.group(0)), masked)

    for _, date_str in datefinder.find_dates(masked, source=True):
        print(date_str)
        if date_str[:3] in ('on ', 'at '):
            date_str = date_str[3:]
        locations.extend(_find_all(masked, date_str))
        masked = masked.replace(date_str, '*' * len(date_str))
    
    locations.sort(key=itemgetter(0))
    
    result = []
    advanced = 0
    for start, end in locations:
        result.append((text[advanced:start], False))
        result.append((text[start:end], True))
        advanced=end
    if text[advanced:]:
        result.append((text[advanced:], False))
    return result
