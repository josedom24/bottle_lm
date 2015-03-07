from bottle import Bottle,route,run,request,template
@route('/hello')
@route('/hello/')
@route('/hello/<name>')
def hello(name='Mundo'):
    return template('template_hello.tpl', nombre=name)

run(host='0.0.0.0', port=8080)
