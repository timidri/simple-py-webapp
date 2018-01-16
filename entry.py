from templite import Templite

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h1 style='color:blue'>Hello There!</h1>"]

def test():
    tpl = (1,2,3,4)
    return t(tpl=tpl)

page_template="""<html>
<head>
  <title>Puppet Demo</title>
</head>
     <body>
         <ul>
${
for it in tpl:
    emit("<li>")
    emit(it)
    emit("</li>")
}$
        ${emit("hi")}$
    </body>
</html>"""
