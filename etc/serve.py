#!/usr/bin/env python
import CGIHTTPServer
import webbrowser
import os

from etc import compile_html


def main():
    compile_html.compile_html()

    # run CGI enabled server
    server_address = ('', 8000)
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    handler.cgi_directories = ['/cgi-bin']
    server = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, handler)
    try:
        # look in output folder for index.html
        os.chdir(os.path.join(os.path.abspath(os.curdir), 'output'))
        # open browser at server location
        webbrowser.open('http://localhost:8000/', new=2)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()




