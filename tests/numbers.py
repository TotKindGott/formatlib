# coding: utf-8

import formatlib as fl
import datetime as dt

n = dt.datetime.now()
d = dt.date.today()
t = dt.timedelta(days=3, minutes=195)

def border():
  print '*'*42
  
print 'formatlib.numbers test'.center(42)
print

border()

print fl.hours_output.__doc__
print '>>> t = datetime.timedelta(days=3, minutes=195)\n>>> fl.hours_output(t) \n\t', fl.hours_output(t), '\n'

border()

print fl.time_output.__doc__
print '>>> fl.time_output(hours=2, minutes=29) \n', '\t', fl.time_output(hours=2, minutes=29), '\n'

border()

print fl.date_only.__doc__
print '>>> fl.date_only(n) \nn =', n, '\t', fl.date_only(n), '\n'

border()

print fl.time_only.__doc__
print '>>> fl.time_only(n) \nn =', n, '\t',  fl.time_only(n), '\n'
print '>>> fl.time_only(n, 12) \nn =', n, '\t', fl.time_only(n, 12), '\n'

border()

print fl.zero_lead.__doc__
print '>>> fl.zero_lead(2) \t\t', fl.zero_lead(2)
print '>>> fl.zero_lead(12) \t\t', fl.zero_lead(12)
print '>>> fl.zero_lead(2,3) \t\t', fl.zero_lead(2,3), '\n'

border()

print fl.zero_trail.__doc__
print '>>> fl.zero_trail(2) \t\t', fl.zero_trail(2)
print '>>> fl.zero_trail(12,3) \t\t', fl.zero_trail(12,3)
print '>>> fl.zero_trail(2.75432,3) \t\t', fl.zero_trail(2.75432,3), '\n'

border()