#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

from getpass import getpass
from fabric import Connection

def remote_server():
    host = input('Enter host address: ')
    user = input('Enter user name: ')
    password = getpass('Enter password: ')

    # Establish a connection
    conn = Connection(host=host, user=user, connect_kwargs={'password': password})

    return conn

def install_package(conn):
    conn.run("pip install yolk")

if __name__ == '__main__':
    # Example usage
    remote_conn = remote_server()
    install_package(remote_conn)
