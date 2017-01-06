# coding: utf-8

import os
import formatlib as fl
import datetime
from highlight import highlight

MODULE = 'formatlib'

n = datetime.datetime.now()
d = datetime.date.today()
td = datetime.timedelta(days=3, minutes=195)
dt = datetime.datetime(2016,1,1,17,0,0)


def border():
  highlight('*'*42, 'blue', False)
  

def simulate_console_function(function, args, module=MODULE, comment=None):
  highlight('>>> ' + module + '.', 'white')
  highlight(function, 'orange')
  highlight('(', 'white')
  if args:
    if str.isdigit(str(args[0])) or isinstance(args[0], (int, float)):
      highlight(args[0], 'yellow')
    else:
      try:
        args[0].index('=')
        l, r = args[0].split('=')
        highlight(l + '=', 'white')
        if str.isdigit(r):
          highlight(r, 'yellow')
        else:
          highlight(r, 'green')
      except:
        highlight(args[0], 'green')
    for each in args[1:]:
      highlight(', ', 'white')
      if str.isdigit(str(each)):
        highlight(each, 'yellow')
      else:
        try:
          each.index('=')
          l, r = each.split('=')
          highlight(l + '=', 'white')
          if str.isdigit(r):
            highlight(r, 'yellow')
          else:
            highlight(r, 'green')
        except:
          highlight(args[0], 'green')
    highlight(')', 'white')
  if comment:
    highlight(' # ' + comment, 'gray')
  print


def simulate_console_statement(varname, function=None, args=[], assign='', module=None, comment=None):
  highlight('>>> ' + varname + ' = ', 'white')
  if module:
    print module + '.',
  if function:
    highlight(function, 'orange')
    highlight('(', 'white')
    if args:
      if str.isdigit(str(args[0])) or isinstance(args[0], (int, float)):
        highlight(args[0], 'yellow')
      else:
        try:
          args[0].index('=')
          l, r = args[0].split('=')
          highlight(l + '=', 'white')
          if str.isdigit(r):
            highlight(r, 'yellow')
          else:
            highlight(r, 'green')
        except:
          highlight(args[0], 'green')
      for each in args[1:]:
        highlight(', ', 'white')
        if str.isdigit(str(each)):
          highlight(each, 'yellow')
        else:
          try:
            each.index('=')
            l, r = each.split('=')
            highlight(l + '=', 'white')
            if str.isdigit(r):
              highlight(r, 'yellow')
            else:
              highlight(r, 'green')
          except:
            highlight(args[0], 'green')
    highlight(')', 'white')
  elif assign:
    if isinstance(assign, (int, float)):
      highlight(assign, 'yellow')
    else:
      highlight(assign, 'green')
  if comment:
    highlight(' # ' + comment, 'gray')
  print


highlight('- formatlib.numbers -'.center(42), 'green', False)
print

border()

print fl.zero_lead.__doc__

simulate_console_function('zero_lead', [2], comment=fl.zero_lead(2))
simulate_console_function('zero_lead', [12], comment=fl.zero_lead(12))
simulate_console_function('zero_lead', [2,3], comment=fl.zero_lead(2,3))

print

border()

print fl.zero_trail.__doc__

simulate_console_function('zero_trail', [2], comment=fl.zero_trail(2))
simulate_console_function('zero_trail', [12,3], comment=fl.zero_trail(12,3))
simulate_console_function('zero_trail', [2.75432,3], comment=fl.zero_trail(2.75432,3))

print

border()

print fl.hours_output.__doc__

simulate_console_statement(varname='td', module='datetime', function='timedelta', args=['days=3', 'minutes=195'])
simulate_console_function('hours_output', ['td'], comment=fl.hours_output(td))

print 

border()

print fl.time_output.__doc__

simulate_console_function('time_output', ['hours=2', 'minutes=29'], comment=fl.time_output(hours=2, minutes=29))
simulate_console_function('time_output', ['seconds=12345'], comment=fl.time_output(seconds=12345))

print 

border()

print fl.time_output.__doc__

simulate_console_statement(varname='dt', module='datetime', function='datetime', args=[2016,1,1,17,0,0])
simulate_console_function('date_only', ['dt'], comment=fl.date_only(dt))

print

border()

print fl.time_only.__doc__

simulate_console_statement(varname='dt', module='datetime', function='datetime', args=[2016,1,1,17,0,0])
simulate_console_function('time_only', ['dt'], comment=fl.time_only(dt))
simulate_console_function('time_only', ['dt',12], comment=fl.time_only(dt,12))

print 

border()

print fl.last_modified.__doc__

simulate_console_statement('files', 'listdir', ["'.'"], module='os')
simulate_console_statement('file', assign='files[0]', comment=os.listdir('.')[0])
simulate_console_function('last_modified', ['file'], comment=fl.last_modified(os.listdir('.')[0]))
print

border()
