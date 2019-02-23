import fileinput
import datetime
import PyRSS2Gen
import sys
import pdb

def main():
    # create output feed
    rss = PyRSS2Gen.RSS2(
        title = "{{{FEEDNAME}}}",
        link = "",
        description = "",
        lastBuildDate = datetime.datetime.now())

    # parse input lines
    for line in fileinput.input():
        (title,
         link,
         description,
         updated) = line.split("\t")

        # insert item into output feed
        rss.items.append(
            PyRSS2Gen.RSSItem(
                title = title,
                link = link,
                description = description,
                pubDate = updated))

    # done, write out entire feed
    rss.write_xml(sys.stdout)

if (__name__ == "__main__"):
    main()
