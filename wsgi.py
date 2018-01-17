from templite import Templite

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = get_text()
    return [txt]

def get_header():
    t = Templite(header_template)
    title = "Default Page Title"
    return t.render(title=title)

def get_body():
    t = Templite(body_template)
    return t.render()

def construct_page():
    header = get_header()
    body = get_body()
    t = Templite(page_template)
    return t.render(header=header, body=body)

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = construct_page()
    return [txt]

header_template = """
    <title> ${ write(title) }$ </title>
"""

body_template = """
<p>This is a test</p>
"""

page_template = """
<html>
    <head>
${write(header)}$
    </head>
    <body>
${write(body)}$
    </body>
</html>
"""

print construct_page()