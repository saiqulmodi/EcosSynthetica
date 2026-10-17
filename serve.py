"""Start Ecos-Synthetica on this PC: picks a free port, serves the game folder
and opens it in the browser. Close this window to stop the game server."""
import functools
import http.server
import socket
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def free_port(start=8765):
    for port in range(start, start + 200):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise RuntimeError("No free port found")


def main():
    port = free_port()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"Ecos-Synthetica is running at {url}")
    print("Close this window to stop it.")
    webbrowser.open(url)
    server.serve_forever()


if __name__ == "__main__":
    main()
