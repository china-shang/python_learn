#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server
import test_openssl
import ssl
#import SocketServer
import requests

PORT = 9090


class handler(http.server.BaseHTTPRequestHandler):
    def do_PUT(self):
        print(self.command)

    def do_CONNECT(self):
        print("do_CONNECT")
        host, _, port = self.path.rpartition(':')
        port = int(port)
        certfile = test_openssl.get_crt(host)
        self.__realconnection = None
        print("write 200 OK")
        self.wfile.write(b'HTTP/1.1 200 OK\r\n\r\n')

        print("start wrap_socket")
        try:
            ssl_sock = ssl.wrap_socket(
                self.connection, keyfile=certfile, certfile=certfile, server_side=True)
        except ssl.SSLError as e:
            return
        except Exception as e:
            print(e)
            return
        print("end wrap_socket")
        self.__realconnection = self.connection
        self.__realwfile = self.wfile
        self.__realrfile = self.rfile
        self.connection = ssl_sock
        self.rfile = self.connection.makefile('rb', 256 * 1024)
        self.wfile = self.connection.makefile('wb', 0)
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return
        except Exception as e:
            # a read or a write timed out.  Discard this connection
            #self.log_error("Request timed out: %r", e)
            print(e)
            print("close connection")
            self.close_connection = True

        if self.__realconnection:
            try:
                self.__realconnection.shutdown(socket.SHUT_WR)
                self.__realconnection.close()
            except Exception:
                pass
            finally:
                self.__realconnection = None
        print(self.headers)
        print(self.path)
        print(self.command)
        #self.wfile.write(b'HTTP/1.1 404 Not Found\r\n\r\n')

        url = self.path
        if url.startswith('/'):
            url = 'https://' + self.headers['Host'] + '/'
        response = requests.get(
            url,
            headers=self.headers,
            # data=self.send_response,
            timeout=3)
        #self.send_header('Content-type', 'text/html')
        print(response.status_code)
        #self.send_response(response.status_code)
        #for i in response.headers.items():
            #self.send_header(i[0], i[1])
            #print(i[0], ":", i[1])
        #self.end_headers()
        self.wfile.write(response.content)
        print(response.content)

        return

    def do_GET(self):

        # Send headers

        print("this in do_GET")
        response = requests.get(
            self.path,
            headers=self.headers,
            # data=self.send_response,
            timeout=5)
        self.send_response(response.status_code)
        print(response.headers)
        for i in response.headers.items():
            print(i[1])
            self.send_header(i[0], i[1])
        self.end_headers()
        self.wfile.write(response.content)
        print(self.command)


server = http.server.HTTPServer(('127.0.0.1', PORT), handler)
server.serve_forever()
