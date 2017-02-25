# formatlib
conversions and various output formats for colors, data sizes, date/time etc.

## formatlib.numbers
`zero_lead(num, shift=2)` - returns number with a leading zero. Optional shift argument defines the length, default value is 2.
`zero_trail(num, shift=2)` - returns number with a set precision after comma, default value is 2.
`hours_output(delta)`- transforms datetime.timedelta object into a string in format '[h+]hh:mm'.
`time_output(weeks=0, days=0, hours=0, minutes=0, seconds=0)`- accepts following arguments: weeks, days, hours, minutes, seconds. Returns time in format [00:][00:]00:00:00.
`date_only(datetime_obj)`- extracts from datetime (or date) object and returns date in format [MM:DD].
`time_only(datetime_obj, time_format=24)` - extracts from datetime object and returns time in format [hh:mm]. Can be 24-hour or 12-hour output with [am/pm] indicator.
`last_modified(file)` - Returns human-readable string containing relative time of the last modification of specified file.
`human_size(size)` - returns the size of a file in human-readable format.


