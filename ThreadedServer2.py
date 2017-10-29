# wx_ipc.py

import select
import socket
import time
import sys

from threading import Thread

HOST = 'localhost'
PORT = 2000



class IPCThread(Thread):
    # ----------------------------------------------------------------------
    def __init__(self):
        """Initialize"""
        Thread.__init__(self)

        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        # Setup TCP socket
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)
        self.setDaemon(True)
        self.start()

    # ----------------------------------------------------------------------
    def run(self):
        """
        Run the socket "server"
        """
        while True:
            try:
                client, addr = self.socket.accept()
                ready = select.select([client, ], [], [], 2)
                if ready[0]:
                    recieved = client.recv(4096)
                    print (recieved)
                    # wx.CallAfter(Publisher().sendMessage, "update", recieved)
            except socket.error:
                msg1 = "Socket error! "
                print(msg1)
                break
        # shutdown the socket
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except:
            pass
        self.socket.close()

if __name__ == '__main__':
    try:
        ipc = IPCThread()
        print("started thread")
        while 1:
            time.sleep(5)
            print("waiting for commands")
    except KeyboardInterrupt:  # catch control-c
        print("cleanly closing.")
        sys.exit(0)