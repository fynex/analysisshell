import socket
import requests
import json


def json_post(url, json_dict):
    #header = {"Content-Type": "application/json;charset=utf-8"}
    header = {"Content-Type": "application/json"}

    return requests.post(url, headers=header, data=json.dumps(json_dict)).text


def single_send(ip, port, data, receive_size=2048, timeout_sec=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((ip,port))
    s.settimeout(timeout_sec)
    s.sendall(data)
    try:
        response = s.recv(receive_size)
    except socket.timeout:
        return None
    finally:
        s.close()

    return response

def mass_send(ip_list, port_list, data, receive_size=2048, timeout_sec=5):
    for ip in ip_list:
        for port in port_list:
            print single_send(ip, int(port), data, receive_size)

