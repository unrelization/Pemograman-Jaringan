#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

import smtpd
import asyncore
import argparse
import threading

class CustomSMTPServer(smtpd.SMTPServer):
    def __init__(self, localaddr, remoteaddr):
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr)

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Message Received from:', peer)
        print('From:', mailfrom)
        print('To :', rcpttos)
        print('Message :', data)
        return

def run_smtp_server(host, port):
    server = CustomSMTPServer((host, port), None)
    asyncore.loop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mail Server Example')
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()

    smtp_thread = threading.Thread(target=run_smtp_server, args=(given_args.host, given_args.port))
    smtp_thread.start()
    smtp_thread.join()
