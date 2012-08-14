#! /usr/bin/python

import logging
import os
import socket
import CandlepinTest as cpt

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-f", "--log-file", dest="log_file",
                      help="log file name", default="log/flooder.log")
    parser.add_option("-c", "--candlepin_hostname", dest="candlepin_hostname",
                      help="candlepin hostname", default=socket.gethostname())
    (options, args) = parser.parse_args()

    # ======== Setup ========
    fp = options.log_file[:options.log_file.rfind("/")]    

    if not os.path.exists(fp):
        os.makedirs(fp)
    logging.basicConfig(filename=options.log_file, level=logging.DEBUG)
    logging.info('Logging to: %s' % options.log_file)

    # ======== Run & Collect Data ========
    # 
    # Set #1: Candlepin Functionalities
    logging.info('Starting candlepin test functionalities.')
    cp = cpt.CandlepinTest(host=options.candlepin_hostname, server_prefix='katello/api', username='admin', password='admin')
    cp.register(name='test_sytem', facts={'core': 1})
    cp.subscribe()
    # Set #2: Pulp Functionalities
    # Set #3: Katello Functionalities

if __name__ == "__main__":
    main()
