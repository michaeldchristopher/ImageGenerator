#! /usr/bin/env python

import socketserver, subprocess, sys
from threading import Thread
import shlex
import time

my_unix_command = ['ls']
HOST = 'localhost'
PORT = 2000


def processCommand(cmd):
    if cmd[0] == "a":
        print("show alpha.jpg")
        return "command a processed"
    elif cmd[0] == 'z':
        print("show zed.jpg")
        return "command z processed"
    return "command NOT processed"


class SingleTCPHandler(socketserver.BaseRequestHandler):
    "One instance per connection.  Override handle(self) to customize action."

    def handle(self):
        # self.request is the client connection
        data = self.request.recv(1024)  # clip input at 1Kb
        data = data.decode("utf-8")  # convert from bytes to a string
        data = data.strip()
        reply = processCommand(data)  # run the one letter command
        if reply is not None:
            reply = "\n" + reply + "\n"
            reply = reply.encode("utf-8")  # convert to bytes
            self.request.send(reply)
        self.request.close()


class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    allow_reuse_address = True
    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)


if __name__ == "__main__":
    try:
        server = SimpleServer((HOST, PORT), SingleTCPHandler)
        server.serve_forever()
        print("passed serve forever")
    except KeyboardInterrupt:  # catch control-c
        print("cleanly closing.")
        sys.exit(0)
    time.sleep(5)
    server.server_close()
    print("closing by time out")
    sys.exit(1)