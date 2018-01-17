def get_head(env={}):
    title = "Default Page Title"
    return head_template.format(title)

def get_body(env={}):
    table_rows = []
    for (key, value) in sorted(env.items()):
        line = '<tr{2}><td>{0}</td><td>{1}</td></tr>'.format(key, value, key == 'uwsgi.node'?' class="id"':''))
        table_rows.append(line)
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
<style type='text/css'>
  table {{
      border: 1px solid black;
      border-collapse: collapse;
  }}
  td {{
      border: 1px dotted gray;
  }}

  .id {{
      font-weight: bold;
      color: red;
  }}
</style>
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
