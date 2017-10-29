# This server processes commands to show requested images
# Michael Christopher
# copyright 2017


import threading
import socketserver
import time
import ShowPicture
import socket

class FileServerHandler(socketserver.StreamRequestHandler):
    def handle(self):
        global mygui
        while True:
            #data = self.request.recv(1024)
            data = self.rfile.readline()
            if not data:
                break  # the other side disconnected
            cmd = str(data.strip(), 'ascii')
            l = cmd.split()
            if len(l) == 2:
                if l[0] == "showimage" or l[0] == "si":
                    mygui.ChooseImage(l[1])
                else:
                    print("Unknown command. Expected si filename.jpg. Got %s" % cmd)
            cur_thread = threading.currentThread()
            response = '\n%s: %s\n' % (cur_thread.getName(), data)
            self.wfile.write(response.encode("utf-8"))  # convert to bytes
        print("client disconnected")

class ThreadedPictureServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def clientSendReceive(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        print('Sent : "%s"' % message)
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))
        return response

if __name__ == '__main__':
    global BailOut
    BailOut = False

    HOST, PORT = "localhost", 2000
    address = (HOST, PORT)  # let the kernel give us a port
    server = ThreadedPictureServer(address, FileServerHandler)
    ip, port = server.server_address  # find out what port we were given
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # don't hang on exit
    t.allow_reuse_address = True
    t.start()
    print('Server loop running in thread:', t.getName())

    global mygui
    mygui = ShowPicture.GUI()
    mygui.SpinUpGui()
    server.socket.close()  # Clean up
