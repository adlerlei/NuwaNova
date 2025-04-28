from http.server import BaseHTTPRequestHandler, HTTPServer

# 讀取 .nuwa 語法，建立路由對應表
routes = {}
with open('script.nuwa', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

i = 0
while i < len(lines):
    if lines[i].startswith("route") and i + 1 < len(lines):
        path = lines[i].split("'")[1]
        if lines[i+1].startswith("respond"):
            response = lines[i+1].split("'")[1]
            routes[path] = response
            i += 2
        else:
            i += 1
    else:
        i += 1

# 處理 HTTP 請求
class NuwaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = routes.get(self.path, "404 Not Found - Nuwa didn't plan this path.")
        self.send_response(200 if self.path in routes else 404)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

# 啟動伺服器
def run():
    server = HTTPServer(('localhost', 8000), NuwaHandler)
    print("Nuwa Web Server is running at http://localhost:8000/")
    server.serve_forever()

if __name__ == '__main__':
    run()