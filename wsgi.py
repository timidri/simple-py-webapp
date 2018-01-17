def get_head(env={}):
    title = "Default Page Title"
    return head_template.format(title)

def get_body(env={}):
    table_rows = [
        '<tr><td>%s</td><td>%s</td></tr>' % (key, value) for key, value in sorted(env.items())
    ]
    table = '\n'.join(table_rows)
    body = body_template.format(table)

    return body

def construct_page(env={}):
    head = get_head(env)
    body = get_body(env)
    page = page_template.format(head,body)
    return page

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = construct_page(env)
    return [txt]

head_template="""
<title>{0}</title>
"""

body_template="""
<div>
  <table>
    {0}
  </table>
</div>
"""

page_template="""
<html>
<head>
{0}
</head>
<body>
{1}
</body>
</html>
"""

env = {
    "left": 1,
    "right": 2,
    "up": 3,
    "down": 4
}
#print construct_page(env)
