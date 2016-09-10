# coding: utf-8

from .numbers import zero_lead

__all__ = ['hex_to_rgb', 'rgb_to_hex',
           'rgb_to_num', 'num_to_rgb',
           'color_names', 'color_groups']

"""
Named HTML color variations & their HEX vaues as defined by W3C,
and functions to convert between color formats.
"""

color_names = dict()

# Source: http://www.w3schools.com/colors/colors_groups.asp

pink_group = {
   'Pink': '#FFC0CB',
   'LightPink': '#FFB6C1',
   'HotPink': '#FF69B4',
   'DeepPink': '#FF1493',
   'PaleVioletRed': '#DB7093',
   'MediumVioletRed': '#C71585'
}

purple_group = {
   'Lavender': '#E6E6FA',
   'Thistle': '#D8BFD8',
   'Plum': '#DDA0DD',
   'Orchid': '#DA70D6',
   'Violet': '#EE82EE',
   'Fuchsia': '#FF00FF	',
   'Magenta': '#FF00FF	',
   'MediumOrchid': '#BA55D3',
   'DarkOrchid': '#9932CC',
   'DarkViolet': '#9400D3',
   'BlueViolet': '#8A2BE2',
   'DarkMagenta': '#8B008B',
   'Purple': '#800080',
   'MediumPurple': '#9370DB',
   'MediumSlateBlue': '#7B68EE',
   'SlateBlue': '#6A5ACD',
   'DarkSlateBlue': '#483D8B',
   'RebeccaPurple': '#663399',
   'Indigo': '#4B0082'
}

red_group = {
   'LightSalmon': '#FFA07A',
   'Salmon': '#FA8072',
   'DarkSalmon': '#E9967A',
   'LightCoral': '#F08080',
   'IndianRed': '#CD5C5C',
   'Crimson': '#DC143C',
   'Red': '#FF0000',
   'FireBrick': '#B22222',
   'DarkRed': '#8B0000'
}

orange_group = {
   'Orange': '#FFA500',
   'DarkOrange': '#FF8C00',
   'Coral': '#FF7F50',
   'Tomato': '#FF6347',
   'OrangeRed': '#FF4500'
}

yellow_group = {
   'Gold': '#FFD700',
   'Yellow': '#FFFF00',
   'LightYellow': '#FFFFE0',
   'LemonChiffon': '#FFFACD',
   'LightGoldenRodYellow': '#FAFAD2',
   'PapayaWhip': '#FFEFD5',
   'Moccasin': '#FFE4B5',
   'PeachPuff': '#FFDAB9',
   'PaleGoldenRod': '#EEE8AA',
   'Khaki': '#F0E68C',
   'DarkKhaki': '#BDB76B'
}

green_group = {
   'GreenYellow': '#ADFF2F',
   'Chartreuse': '#7FFF00',
   'LawnGreen': '#7CFC00',
   'Lime': '#00FF00',
   'LimeGreen': '#32CD32',
   'PaleGreen': '#98FB98',
   'LightGreen': '#90EE90',
   'MediumSpringGreen': '#00FA9A',
   'SpringGreen': '#00FF7F',
   'MediumSeaGreen': '#3CB371',
   'SeaGreen': '#2E8B57',
   'ForestGreen': '#228B22',
   'Green': '#008000',
   'DarkGreen': '#006400',
   'YellowGreen': '#9ACD32',
   'OliveDrab': '#6B8E23',
   'DarkOliveGreen': '#556B2F',
   'MediumAquaMarine': '#66CDAA',
   'DarkSeaGreen': '#8FBC8F',
   'LightSeaGreen': '#20B2AA',
   'DarkCyan': '#008B8B',
   'Teal': '#008080'
}

cyan_group = {
   'Aqua': '#00FFFF',
   'Cyan': '#00FFFF',
   'LightCyan': '#E0FFFF',
   'PaleTurquoise': '#AFEEEE',
   'Aquamarine': '#7FFFD4',
   'Turquoise': '#40E0D0',
   'MediumTurquoise': '#48D1CC',
   'DarkTurquoise': '#00CED1'
}

blue_group = {
   'CadetBlue': '#5F9EA0',
   'SteelBlue': '#4682B4',
   'LightSteelBlue': '#B0C4DE',
   'LightBlue': '#ADD8E6',
   'PowderBlue': '#B0E0E6',
   'LightSkyBlue': '#87CEFA',
   'SkyBlue': '#87CEEB',
   'CornflowerBlue': '#6495ED',
   'DeepSkyBlue': '#00BFFF',
   'DodgerBlue': '#1E90FF',
   'RoyalBlue': '#4169E1',
   'Blue': '#0000FF',
   'MediumBlue': '#0000CD',
   'DarkBlue': '#00008B',
   'Navy': '#000080',
   'MidnightBlue': '#191970'
}

brown_group = {
   'Cornsilk': '#FFF8DC',
   'BlanchedAlmond': '#FFEBCD',
   'Bisque': '#FFE4C4',
   'NavajoWhite': '#FFDEAD',
   'Wheat': '#F5DEB3',
   'BurlyWood': '#DEB887',
   'Tan': '#D2B48C',
   'RosyBrown': '#BC8F8F',
   'SandyBrown': '#F4A460',
   'GoldenRod': '#DAA520',
   'DarkGoldenRod': '#B8860B',
   'Peru': '#CD853F',
   'Chocolate': '#D2691E',
   'Olive': '#808000',
   'SaddleBrown': '#8B4513',
   'Sienna': '#A0522D',
   'Brown': '#A52A2A',
   'Maroon': '#800000'
}

white_group = {
   'White': '#FFFFFF',
   'Snow': '#FFFAFA',
   'HoneyDew': '#F0FFF0',
   'MintCream': '#F5FFFA',
   'Azure': '#F0FFFF',
   'AliceBlue': '#F0F8FF',
   'GhostWhite': '#F8F8FF',
   'WhiteSmoke': '#F5F5F5',
   'SeaShell': '#FFF5EE',
   'Beige': '#F5F5DC',
   'OldLace': '#FDF5E6',
   'FloralWhite': '#FFFAF0',
   'Ivory': '#FFFFF0',
   'AntiqueWhite': '#FAEBD7',
   'Linen': '#FAF0E6',
   'LavenderBlush': '#FFF0F5',
   'MistyRose': '#FFE4E1'
}

grey_group = {
   'Gainsboro': '#DCDCDC',
   'LightGray': '#D3D3D3',
   'Silver': '#C0C0C0',
   'DarkGray': '#A9A9A9',
   'DimGray': '#696969',
   'Gray': '#808080',
   'LightSlateGray': '#778899',
   'SlateGray': '#708090',
   'DarkSlateGray': '#2F4F4F',
   'Black': '#000000'
}

color_groups = {
  'pink_group': pink_group,
  'red_group': red_group,
  'orange_group': orange_group,
  'yellow_group': yellow_group,
  'green_group': green_group,
  'cyan_group': cyan_group,
  'blue_group': blue_group,
  'brown_group': brown_group,
  'white_group': white_group,
  'grey_group': grey_group
}

for each_group in color_groups.values():
    color_names.update(each_group)


def color_palette(*args):

    """
    Prints out names, (hex and/or RGB and/or numerical values)
    for each of the web-safe HTML-supported colors, in color.
    """

    from highlight import highlight

    for color_name, hex_value in color_names.items():
        c = convert_color(hex_value, 'num')
        highlight(' '+color_name+' ', c, False, fill='#',
                  width=42, alignment='center')
        if 'hex' in args:
            highlight(hex_value, c, False, width=42, alignment='center')
        if 'rgb' in args:
            highlight(convert_color(hex_value, 'rgb'), c, False,
                      width=42, alignment='center')
        if 'num' in args:
            highlight(convert_color(hex_value, 'num'), c, False,
                      width=42, alignment='center')
  

def hex_to_rgb(color):
    
    """
    Accepts a hex color as a string, returns a tuple of RGB values.
    """
  
    color = color.lstrip('#')
    if len(color) == 3:
        return tuple(int(str(each*2), 16) for each in color)
    elif len(color) == 6:
        return tuple(int(n, 16) for n in (color[0:2], color[2:4], color[4:6]))
    else:  # Wrong argument format.
        raise TypeError('hex string expected')


def rgb_to_hex(*arg):
    
    """
    Accepts three RGB values in range (0..255) as separate arguments
    or a list/tuple, returns a hex string.
    """
  
    result = '#'
    if len(arg) == 3:
        for each in arg:
            result += zero_lead('{0:x}'.format(int(each)))
    elif isinstance(arg[0], (list, tuple)):
        for each in arg[0]:
            n = '{0:x}'.format(int(each))
            result += n if len(str(n)) == 2 else '0' + n
    else:  # Wrong aegument format.
        raise TypeError('sequence of RGB values expected')
    return result.upper()


def rgb_to_num(*arg):
    
    """
    Accepts three RGB values in range (0..255) as separate arguments
    or a list/tuple, returns a tuple with numerical values in range (0..1).
    """
  
    if len(arg) == 3:
        return tuple(round(float(each) / 255, 3) for each in arg)
    elif isinstance(arg[0], (list, tuple)):
        return tuple(round(float(each) / 255, 3) for each in arg[0])
    else:  # Wrong argument format.
        raise TypeError('sequence of RGB vaues expected')


def num_to_rgb(*arg):
    
    """
    Accepts three numerical values in range (0..1) as separate arguments
    or a list/tuple, returns a tuple with RGB values in range (0..255).
    """
  
    if len(arg) == 3:
        return tuple(int(each * 255) for each in arg)
    elif isinstance(arg[0], (list, tuple)):
        return tuple(int(each * 255) for each in arg[0])
    else:  # Wrong argument format.
        raise TypeError('sequence of numerical values expected')


def convert_color(color, format):
    
    """
    Supports conversion to and from RGB, hex and numerical in range (0..1).
    Accepts following arguments:
      color - string for hex, list/tuple for rgb or num.
      format - conversion format ('rgb', 'hex' or 'num').
    Built on top of individual conversion functions:
      hex_to_rgb() & rgb_to_hex() and
      rgb_to_num() & num_to_rgb().
    """

    formats = ('hex', 'rgb', 'num')

    # Verify the conversion format.
    if format.lower() in formats:
        format_out = format

    # Determine format_in.
    if isinstance(color, str):
        format_in = 'hex'
    elif isinstance(color, (list, tuple)):
        if color[0] <= 1.0 and color[1] <= 1.0 and color[2] <= 1.0:
            format_in = 'num'
        else:
            format_in = 'rgb'
    else:
        return None

    # Perform the conversion.
    if format_in == 'hex':
        if format_out == 'rgb':
            return hex_to_rgb(color)
        elif format_out == 'num':
            return rgb_to_num(hex_to_rgb(color))
        else:
            return color
    elif format_in == 'rgb':
        if format_out == 'hex':
            return rgb_to_hex(color)
        elif format_out == 'num':
            return rgb_to_num(color)
        else:
            return color
    elif format_in == 'num':
        if format_out == 'rgb':
            return num_to_rgb(color)
        elif format_out == 'hex':
            return rgb_to_hex(num_to_rgb(color))
        else:
            return color

