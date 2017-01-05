# coding: utf-8

"""
Number Output Format Library.

    Number output formatting, i.e.
    "001" with zero_lead(1,3) and
    "1.50" with zero_trail(1.5,2) for aligning tables etc.
    Time difference formatting, i.e. "01:23:45" with time_output(seconds=5025).
"""

__all__ = ['zero_lead', 'hours_output',
           'zero_trail', 'time_output',
           'date_only', 'time_only',
           'last_modified', 'human_size',
           'percentify']


def zero_lead(num, shift=2):
    
    """
    Returns number with a leading zero.
    Optional shift argument defines the length, default value is 2.
    """
  
    try:
        num = float(num)
        shift = int(shift)
    except Exception:
        raise ValueError('expected arguments of type int or float')
    argument = '0'+str(shift)+'n'
    return format(num, argument)
  

def zero_trail(num, shift=2):
    
    """
    Returns number with a set precision after comma, default value is 2.
    """
  
    # Uses built-in round() function. 
    try:
        num = float(num)
        shift = int(shift)
    except Exception:
        raise ValueError('expected arguments of type int or float')
    argument = '{:.'+str(shift)+'f}'
    return argument.format(num)


def hours_output(delta):
    
    """
    Transforms datetime.timedelta object into a string in format '[h+]hh:mm'.
    """
  
    hours = (delta.days * 24)
    hours += (delta.seconds // 60 // 60)
    minutes = (delta.seconds // 60 % 60)
    hours = (delta.days * 24) + float(delta.seconds // 60 // 60)
    return zero_lead(hours) + ":" + zero_lead(minutes)


def time_output(weeks=0, days=0,
                hours=0, minutes=0,
                seconds=0):

    """
    Accepts following arguments: weeks, days, hours, minutes, seconds.
    Returns time in format [00:][00:]00:00:00.
    """
  
    total = (weeks * 604800) + (days * 86400) + \
    (hours * 3600) + (minutes * 60) + seconds
  
    output = str()
  
    if total >= 604800:
        weeks = total // 604800
        output += '{}:'.format(zero_lead(weeks))
        total = total % 604800
    
    if weeks or total >= 86400:
        days = total // 86400
        output += '{}:'.format(zero_lead(days))
        total = total % 86400

    hours = total // 3600
    total = total % 3600
    output += '{}:'.format(zero_lead(hours))
  
    minutes = total // 60
    seconds = total % 60
    output += '{}:'.format(zero_lead(minutes))
    output += '{}'.format(zero_lead(seconds))
  
    return output
  

def date_only(datetime_obj):
    
    """
    Extracts from datetime (or date) object and returns date in format [MM:DD].
    """
  
    return zero_lead(datetime_obj.month) + '/' + zero_lead(datetime_obj.day)
  

def time_only(datetime_obj, time_format=24):
    
    """
    Extracts from datetime object and returns time in format [hh:mm].
    Can be 24-hour or 12-hour output with [am/pm] indicator.
    """
  
    if time_format is 12:
        return datetime_obj.strftime("%I:%M %p")
    else:
        return zero_lead(datetime_obj.hour) + ':' + \
            zero_lead(datetime_obj.minute)


def last_modified(file):
    
    """
    Returns human-readable string containing relative time
    of the last modification of specified file.
    """
  
    from os import path
    from datetime import datetime
  
    now = datetime.now()
    modtime = now - datetime.fromtimestamp(path.getmtime(file))
    days = modtime.days + (modtime.seconds / (60 * 60 * 24))
  
    if days:
        if days == 1:
            return 'yesterday'
        elif days == 7:
            return 'a week ago'
        else:
            return str(days) + ' days ago'
    else:
        minutes = modtime.seconds / 60
        if minutes == 0:
            return 'just now'
        elif minutes == 1:
            return '1 minute ago'
        elif minutes < 60:
            return str(minutes) + ' minutes ago'
        else:
            hours = minutes / 60
            if hours == 1:
                return '1 hour ago'
            else:
                return str(hours) + ' hours ago'


def human_size(size):

    """
    Returns human-readable filesize.
    Accepts size in bytes.
    """

    seq = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    unit = seq[0]
    
    while size > 1024:
        size /= 1024.0
        unit = seq[seq.index(unit) + 1]
    
    return '{} {}'.format(round(size, 2), unit)


def percentify(array, precision=2):

    """
    Requires an array with numerical values,
    calculates their percentage against the total array value,
    and returns the exact type array with values replaced.
    Accepted argument types:
        dict, list
    """

    if isinstance(array, list):
        total = sum(array)
        return list(round((100 * float(n)) / total, precision) for n in array) 

    elif isinstance(array, dict):
        total = sum(array[k] for k in array.keys())
        return {k:round((100 * float(array[k])) / total, precision) for k in array.keys()}

    else:
        return None
