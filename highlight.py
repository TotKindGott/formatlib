# coding: utf-8

"""
Text highlighting for iOS-specific module in Pythonista & Editorial apps.
Considering possible merge with bash version of the script.
"""

import sys
import console
from formatlib.numbers import zero_lead, zero_trail

colors = { 
  'blue':   (0.75, 1.00, 1.00),
  'green':  (0.50, 1.00, 0.50),
  'red':    (1.00, 0.25, 0.00),
  'orange': (1.00, 0.50, 0.00),
  'yellow': (1.00, 1.00, 0.00),
  'gray':   (0.50, 0.50, 0.50),
  'purple': (1.00, 0.00, 1.00),
  'white':  (1.00, 1.00, 1.00) 
}


def highlight(text, color, inline=True, alignment='left', width=0, fill=' '):
    
  """
  Accepts following arguments:
      text (required) - string to output to console
      color (required) - text output color
      inline (default=True) - creates a new line after output
      alignment (default='left') - can be also 'right' or 'center'
      width (default=0) - text justification value
  """

  # Does not print any whitespace around the string passed as argument
  
  default_color = colors['white']
  
  def revert_colors(color):
    console.set_color(color[0], color[1], color[2])

  if color in colors.keys():
    console.set_color(colors[color][0], colors[color][1], colors[color][2])
  elif isinstance(color, tuple):
    # unpack the set of RGB values
    if len(color) == 3:
      console.set_color(color[0], color[1], color[2])
    else:
      revert_colors(default_color)
  else:
      revert_colors(default_color)
  
  if alignment == 'right': 
    alignment = '>'
  elif alignment == 'center': 
    alignment = '^'
  else: 
    alignment = '<'
  
  style = str('{:' + fill + alignment + str(width) + '}')
  
  sys.stdout.write(style.format(text))
  
  revert_colors(default_color)
  
  if inline == False:
    print ''  # create a new line


def color_list(filter=None, group=None, value='default'):
  
  """
  Outputs the list of supported colors with their corresponding RGB or HSL values.
  """
  
  for each_color in colors:
    highlight(each_color, color=each_color, width=10, alignment='right')
    print ' (',
    for each_value, value_color in zip(colors[each_color], ((1,0.9,0.9), (0.9,1,0.9), (0.9,0.9,1))):
      highlight(zero_trail(each_value), value_color)
      if value_color != (0.9, 0.9, 1):
        highlight(', ', 'white')
    highlight(') ', 'white')
    highlight('='*10, color=each_color, inline=False, width=10, alignment='right')
  
  print ''


# converter functions were taken from
# http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


if __name__ == '__main__':

  highlight('module highlight', 'green', False)
  print __doc__, '\n'
  
  highlight('function color_list()', 'green', False)
  print color_list.__doc__, '\n'
  
  print '>>> ',
  highlight('highlight.color_list()', 'orange', False)
  color_list()
  
  highlight('function highlight()', 'green', False)
  print highlight.__doc__, '\n'
  
  print '>>> ',
  highlight('highlight.highlight("ATTENTION!", "red", width=42, alignment="center")', 'orange', False)
  highlight("ATTENTION!", "red", False, width=42, alignment='center')
  print 'See console output above for accepted a.k.a web-safe color attributes with their W3C names & respective RGB values'
  
