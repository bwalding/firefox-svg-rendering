#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys


class CORSRequestHandler (SimpleHTTPRequestHandler):
    def get_header(self, path):
        if self.path.find("/strict/") >= 0:
            if self.path.endswith(".svg"):
                return "default-src 'none'; img-src data:"

            return "default-src 'none' 'unsafe-inline'; img-src data: *; style-src: 'unsafe-inline"

        return ""

    def end_headers(self):
        header_value = self.get_header(self.path)
        if header_value != "":
            self.send_header("content-security-policy", header_value)
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(
        sys.argv[1]) if len(sys.argv) > 1 else 8000)
