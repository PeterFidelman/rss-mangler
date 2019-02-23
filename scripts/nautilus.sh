#!/bin/bash
curl 'http://nautil.us/rss/all' |
python3 feed2txt.py |
perl -lne '/^[^\t]+- Issue/ && print "$_"' |
head -n 1 |
perl -lne '/(.*)\t(.*)\t(.*)\t.*, (.*?20[0-9]{2})/ && print "nautil.us Issue $4\t$2\tClick me\t$4"' |
python3 txt2feed.py |
perl -pe 's/{{{FEEDNAME}}}/nautil.us/g'
