# This coding is to make a local backup of following mathematics competition problems and solutions
# provided on AOPS website, in case they do not provide contents in the future, and also for convenience
# to practice the problems on local.
#
# AMC 8
# AMC 10
# AMC 12
# AIME
# USAJMO
# USAMO
#

import urllib.request
import urllib.error
import logging

def crawl_url(url, length, withSeperatedPage):
  filenamebase = url[url.rindex('/') + 1 : ]
  urllib.request.urlretrieve(url, '../html/' + filenamebase + '.html')
  urllib.request.urlretrieve(url + '_Problems', '../html/' + filenamebase + '_Problems' + '.html')
  if (withSeperatedPage):
    urllib.request.urlretrieve(url + '_Answer_Key', '../html/' + filenamebase + '_Answer_Key' + '.html')
  for i in range(length):
    index = str(i + 1)
    logging.info('Downloading ' + url + '_Problems/Problem_' + index, '../html/')
    try:
      urllib.request.urlretrieve(url + '_Problems/Problem_' + index, '../html/' + filenamebase + '_Problem_' + index + '.html')
    except urllib.error.URLError as e:
      logging.warning('Error in Downloading ' + url + '_Problems/Problem_' + index)
      # raise RuntimeError("Failed to download '{}'. '{}'".format(url, e.reason))
      pass

'''
for i in range(1985, 1999):
  index = str(i)
  crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AJHSME', 25, True)

for i in range(1999, 2020):
  index = str(i)
  crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_8', 25, True)

for i in range(2000, 2021):
  index = str(i)
  if (i < 2002):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_10', 25, True)
  else:
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_10A', 25, True)
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_10B', 25, True)
'''
'''
for i in range(1950, 2021):
  index = str(i)
  if (i < 1960):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AHSME', 50, True)
  elif (i < 1968):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AHSME', 40, True)
  elif (i < 1974):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AHSME', 35, True)
  elif (i < 2000):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AHSME', 30, True)
  elif (i < 2002):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_12', 25, True)
  else:
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_12A', 25, True)
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AMC_12B', 25, True)

for i in range(1983, 2021):
  index = str(i)
  if (i < 2000):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AIME', 15, True)
  else:
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AIME_I', 15, True)
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_AIME_II', 15, True)
'''
'''
for i in range(2010, 2021):
  index = str(i)
  crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_USAJMO', 6, False)
'''
for i in range(1972, 2021):
  index = str(i)
  if (i < 1996):
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_USAMO', 5, False)
  else:
    crawl_url('https://artofproblemsolving.com/wiki/index.php/' + index + '_USAMO', 6, False)