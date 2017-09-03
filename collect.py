#!/usr/bin/python

from __future__ import print_function
import sys
import urlparse
import urllib2
import os
import re

def getURL(tag,req,url):
  # now try get the data
  data = req.read()
  # now try to guess the file type
  url_det = urlparse.urlparse(url)
  outfname = os.path.basename(url_det.path)
  mimetype=req.info().gettype()
  if "/" in mimetype:
    [base,suf]=mimetype.split("/")
    suf = "."+suf
  else:
    suf=""
  outfname = "{}{}".format(tag,suf)
  g=open(outfname,"w")
  g.write(data)
  g.close()
  result = "{},{},{}".format(url,outfname,len(data)/1024)
  return result


f = open(sys.argv[1])
for line in f:
    (tag,url)=line.split()
    try:
        req = urllib2.urlopen(url)
        result=getURL(tag,req,url)
    except urllib2.HTTPError as err:
        result=1
        result="{},{},{}{}".format(tag,"FAIL",err.code,err.msg)
    print(result)
f.close()
    
