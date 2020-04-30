#!/usr/bin/env python3
"""
    Advanced Python Programming 31768-931
    Assignment due 4/12/2020
    Write an HTTP service that chooses an available high port number and serves
    a single copy of a memorable text to the first request that comes in.
    Because of firewall rules, requests to services running on hills
    have to come from within the college network
"""

PORT_NO = 9099

MEMORABLE_TXT = """
All the world's a stage,
And all the men and women merely players;
They have their exits and their entrances,
And one man in his time plays many parts,
His acts being seven ages. At first, the infant,
Mewling and puking in the nurse's arms.
Then the whining schoolboy, with his satchel
And shining morning face, creeping like snail
Unwillingly to school. And then the lover,
Sighing like furnace, with a woeful ballad
Made to his mistress' eyebrow. Then a soldier,
Full of strange oaths and bearded like the pard,
Jealous in honour, sudden and quick in quarrel,
Seeking the bubble reputation
Even in the cannon's mouth. And then the justice,
In fair round belly with good capon lined,
With eyes severe and beard of formal cut,
Full of wise saws and modern instances;
And so he plays his part. The sixth age shifts
Into the lean and slippered pantaloon,
With spectacles on nose and pouch on side;
His youthful hose, well saved, a world too wide
For his shrunk shank, and his big manly voice,
Turning again toward childish treble, pipes
And whistles in his sound. Last scene of all,
That ends this strange eventful history,
Is second childishness and mere oblivion,
Sans teeth, sans eyes, sans taste, sans everything.

published 1623 William Shakespear 'As You Like It' Act II Scene VII

"""

import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(MEMORABLE_TXT.encode())

if __name__ == '__main__':
    print("\nTo test the web server's first response,\ntype the following in a new terminal window:")
    print("curl http://hills.ccsf.edu:" + str(PORT_NO) + "\n\n")
    server = ('', PORT_NO)
    httpd = http.server.HTTPServer(server, Handler)
    # Assignment requires only the "first request that comes in" to generate a response
    httpd.handle_request()
