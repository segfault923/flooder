#! /usr/bin/python

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-f", "--log-file", dest="log_file",
                      help="log file name", default="log/doalkcuf.log")
    (options, args) = parser.parse_args()

    # ======== Setup ========
    print options.log_file

if __name__ == "__main__":
    main()
