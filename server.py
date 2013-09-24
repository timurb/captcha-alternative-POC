from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from tokenizer import Tokenizer

def generate(request):
    '''API to generate new token'''
    return Response(tokenizer.generate())

def check(request):
    '''API to check for token correctness'''
    try:
      indx = tokenizer.check_encoded(request.matchdict["token"])
      return Response("Token is found")
    except ValueError:
      return Response("Token is invalid")

if __name__ == '__main__':
    tokenizer = Tokenizer('12345')
    config = Configurator()
    config.add_route('generate', '/generate')
    config.add_route('check', '/check/{token}')
    config.add_view(generate, route_name='generate')
    config.add_view(check, route_name='check')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
