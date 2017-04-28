
def clickjacking_poc(url):
    """<!DOCTYPE html>
    <html>
    <body>

    <iframe src="url">
      <p>Your browser does not support iframes.</p>
    </iframe>

    </body>
    </html>""".format(url)
