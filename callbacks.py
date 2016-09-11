# coding: utf-8

__all__ = ['link_to_maps']


def link_to_maps(address, mode='browser'):
  
  import urllib
  
  if mode is 'app':
    return 'comgooglemaps://?saddr=&daddr=' + urllib.quote(address) + '&directionsmode=driving'
    
  else:
    return 'http://maps.google.com/?q=' + urllib.quote(address)
  

def sync_data():
    
  """
  TimeSheet uses this from within Pythonista app to access Dropbox-synced file through Editorial with x-callback-url request.
  """
  
  import webbrowser, os
  
  from time import sleep

  try:
    # update data from Dropbox via Editorial
    webbrowser.open('editorial://open/checkins.csv?root=dropbox&command=TimeSheet&x-success=pythonista://')
    sleep(10)
    
    # verify the integrity of copied contents
    datafile = os.path.join(os.path.dirname(__file__), 'checkins.csv')
    copied = clipboard.get()
    header = 'date,address,city'
    if copied.startswith(header):
      csvfile = open(datafile, 'w')
      csvfile.write(copied)
      csvfile.close()
    else:
      raise Exception('export error')
  
  except Exception as x:
    raise Exception('sync error', x)
