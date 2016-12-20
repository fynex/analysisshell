import base64
import urllib

def stream_data_base64_encoded(string, url_encode=True):
    base64_str = base64.b64encode(string)
    payload    = "data://text/plain;base64,{}".format(base64_str)

    if url_encode:
        payload = urllib.quote_plus(payload)

    return payload

