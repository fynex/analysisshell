
def clickjacking_poc(url):
    return """<!DOCTYPE html>
    <html>
    <body>

    <iframe src="{}">
      <p>Your browser does not support iframes.</p>
    </iframe>

    </body>
</html>""".format(url)
