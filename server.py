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
      if "encoded" in request.matchdict and request.matchdict["encoded"] == "unencoded":
        check_token = tokenizer.check
      else:
        check_token = tokenizer.check_encoded
      indx = check_token(request.matchdict["token"])
      return Response("Token is found")
    except ValueError:
      return Response("Token is invalid")

if __name__ == '__main__':
    tokenizer = Tokenizer('12345')
    config = Configurator()
    config.add_route('generate', '/generate')
    config.add_route('check', '/check/{token}')
    config.add_route('check_encoded', '/check/{token}/{encoded}')
    config.add_view(generate, route_name='generate')
    config.add_view(check, route_name='check')
    config.add_view(check, route_name='check_encoded')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
