# [formatlib](http://github.com/TotKindGott/formatlib)

[![GitHub forks](https://img.shields.io/github/forks/totkindgott/formatlib.svg)](https://github.com/totkindgott/formatlib/network)
[![GitHub stars](https://img.shields.io/github/stars/TotKindGott/formatlib.svg)](https://github.com/TotKindGott/formatlib/stargazers)

[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/TotKindGott/formatlib.svg)](http://isitmaintained.com/project/TotKindGott/formatlib "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/TotKindGott/formatlib.svg)](http://isitmaintained.com/project/TotKindGott/formatlib "Percentage of issues still open")
[![GitHub issues](https://img.shields.io/github/issues/TotKindGott/formatlib.svg)](https://github.com/TotKindGott/formatlib/issues)

**conversions and various output formats for colors, data sizes, date/time etc.**

## formatlib.numbers
`zero_lead(num, shift=2)` - returns number with a leading zero. Optional shift argument defines the length, default value is 2.  
`zero_trail(num, shift=2)` - returns number with a set precision after comma, default value is 2.  
`hours_output(delta)` - transforms datetime.timedelta object into a string in format '[h+]hh:mm'.  
`time_output(weeks=0, days=0, hours=0, minutes=0, seconds=0)` - accepts following arguments: weeks, days, hours, minutes, seconds. Returns time in format [00:][00:]00:00:00.  
`date_only(datetime_obj)` - extracts from datetime (or date) object and returns date in format [MM:DD].  
`time_only(datetime_obj, time_format=24)` - extracts from datetime object and returns time in format [hh:mm]. Can be 24-hour or 12-hour output with [am/pm] indicator.  
`last_modified(file)` - Returns human-readable string containing relative time of the last modification of specified file.  
`human_size(size)` - returns the size of a file in human-readable format.  

## formatlib.colors
`hex_to_rgb(color)` - accepts a hex color as a string, returns a tuple of RGB values.  
`rgb_to_hex(*arg)` - accepts three RGB values in range (0..255) as separate arguments or a list/tuple, returns a hex string.  
`rgb_to_num(*arg)` - accepts three RGB values in range (0..255) as separate arguments or a list/tuple, returns a tuple with numerical values in range (0..1).  
`num_to_rgb(*arg)` - accepts three numerical values in range (0..1) as separate arguments or a list/tuple, returns a tuple with RGB values in range (0..255).  
`convert_color(color, format)` - supports conversion to and from RGB, hex and numerical in range (0..1). Accepts following arguments:  
    color - string for hex, list/tuple for rgb or num.  
    format - conversion format ('rgb', 'hex' or 'num').  

## formatlib.permissions
`human_mode(path)` - Linux-style human-readable symbolic notation of file permissions.  
 
 