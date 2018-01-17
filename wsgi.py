from templite import Templite

def get_header(env):
    t = Templite(header_template)
    title = "Default Page Title"
    return t.render(title=title)

def get_body(env):
    t = Templite(env_dump_template)
    return t.render(environ=env)

def construct_page(env):
    header = get_header(env)
    body = get_body(env)
    t = Templite(page_template)
    return t.render(header=header, body=body)

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = construct_page(env)
    return [txt]

env_dump_template = """
    <div>
        <ul>
    ${ for key in sorted(environ.items()) }$
            <li>${ key }$</li>
    ${ :end-for }$
        </ul>
    </div>
"""

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

#print construct_page()