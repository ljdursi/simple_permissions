#!/usr/bin/env python3
"""
A toy permissions server which always returns one or no dataset
"""
import argparse
import connexion
from flask import current_app

def permissions(request):
    """
    Mock the behaviour of a permissions server
    """
    user_tokens = request['user_tokens']
    method = request['method']
    path = request['path']

    return {'datasets': current_app.config['RESPONSE']}


def main():
    """
    start the server
    """
    parser = argparse.ArgumentParser(description='Permissions shim.')
    parser.add_argument('--host', default="0.0.0.0", help='host to listen on')
    parser.add_argument('--port', default="8180", help="port to listen on")
    parser.add_argument('--use_tls', action="store_true")
    parser.add_argument('--tls_key', default="/tls.key", help="path to private key")
    parser.add_argument('--tls_cert', default="/tls.crt", help="path to tls cert")
    parser.add_argument('response', nargs='*', default=[])
    args = parser.parse_args()

    options = {"swagger_ui": False}
    app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
    app.add_api("swagger.yaml")

    app.app.config['RESPONSE'] = args.response

    if args.use_tls:
        app.run(host=args.host, port=args.port, ssl_context=(args.tls_cert, args.tls_key))
    else:
        app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
