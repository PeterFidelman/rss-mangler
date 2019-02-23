import feedparser
import fileinput
import sys

def main():
    # Load entire file(s) into memory
    rawdata = ""
    for line in fileinput.input():
        rawdata += line

    # Stuff the resulting buffer into feedparser
    d = feedparser.parse(rawdata)

    # Convert to text
    for entry in d.entries:
        sys.stdout.write("%s\t%s\t%s\t%s\n" %
            (entry.title,
             entry.link,
             sanitize(entry.description),
             entry.updated))

# mediocre "sanitization" function which strips \n and \t
# - \n because our output is line-delimited (one line per feed entry)
# - \t because our output is tab-delimited within each line
def sanitize(s):
    return s.replace("\n", " ").replace("\t", " ")

if (__name__ == "__main__"):
    main()
