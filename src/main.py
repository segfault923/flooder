#! /usr/bin/python

import candlepinTest
import socket

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-f", "--log-file", dest="log_file",
                      help="log file name", default="log/flooder.log")
    parser.add_option("-c", "--candlepin_hostname", dest="candlepin_hostname",
                      help="candlepin hostname", default=socket.gethostname())
    (options, args) = parser.parse_args()

    # ======== Setup ========
    print 'Logging to: ' + options.log_file


    # ======== Run & Collect Data ========
    # 
    # Set #1: Candlepin Functionalities
    candlepinTest.register(host=options.candlepin_hostname, username='admin', password='admin')
    candlepinTest.subscribe()
    # Set #2: Pulp Functionalities
    # Set #3: Katello Functionalities

if __name__ == "__main__":
    main()
