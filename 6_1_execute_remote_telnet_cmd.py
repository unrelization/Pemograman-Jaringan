import getpass
import telnetlib

HOST = "localhost"

def run_telnet_session():
    user = input("Enter your remote account: ")
    password = getpass.getpass()
    session = telnetlib.Telnet(HOST)
    
    session.read_until(b"login: ")
    session.write(user.encode('ascii') + b"\n")
    
    if password:
        session.read_until(b"Password: ")
        session.write(password.encode('ascii') + b"\n")
    
    session.write(b"ls\nexit\n")
    print(session.read_all())

if __name__ == '__main__':
    run_telnet_session()
