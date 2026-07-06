#!/usr/bin/env python3
import argparse
import http.server
import os
import socketserver


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with ReusableTCPServer((args.host, args.port), http.server.SimpleHTTPRequestHandler) as httpd:
        host, port = httpd.server_address
        print("Serving RepoFlow clean-success casebook at http://%s:%s/index.html" % (host, port), flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
