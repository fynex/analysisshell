import socket

def ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None


def hostname(ip):
    try:
        tup      = socket.gethostbyaddr(ip)
        hostname = tup[0]

        return hostname
    except socket.error:
        return None

