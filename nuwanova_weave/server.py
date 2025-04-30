from http.server import BaseHTTPRequestHandler, HTTPServer

# 讀取 .nuwa 語法，建立路由對應表
routes = {}
with open('weave.nuwa', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

i = 0
while i < len(lines):
    if lines[i].startswith("url") and i + 1 < len(lines):
        path = lines[i].split("'")[1]
        route_data = {}
        j = i + 1
        while j < len(lines) and not lines[j].startswith("url"):
            if lines[j].startswith("say"):
                route_data['say'] = lines[j].split("'")[1]
            elif lines[j].startswith("show"):
                route_data['show'] = lines[j].split("'")[1]
            j += 1
        routes[path] = route_data
        i = j
    else:
        i += 1

# 處理 HTTP 請求
class NuwaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/anima/'):
            try:
                file_path = '.' + self.path

                # MIME 類型判斷
                if file_path.endswith('.css'):
                    content_type = 'text/css'
                elif file_path.endswith('.js'):
                    content_type = 'application/javascript'
                elif file_path.endswith('.png'):
                    content_type = 'image/png'
                elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                    content_type = 'image/jpeg'
                elif file_path.endswith('.svg'):
                    content_type = 'image/svg+xml'
                else:
                    content_type = 'application/octet-stream'

                with open(file_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(content)
                return
            except FileNotFoundError:
                self.send_error(404, f'File Not Found: {self.path}')
                return

        route = routes.get(self.path)
        if route is None:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("404 Not Found - Nuwa didn't plan this path.".encode('utf-8'))
            return

        response_parts = []
        content_type = 'text/plain; charset=utf-8'

        if 'say' in route:
            response_parts.append(route['say'])

        if 'show' in route:
            try:
                with open(f'page/{route["show"]}', 'r', encoding='utf-8') as f:
                    html_content = f.read()
                response_parts.append(html_content)
                content_type = 'text/html; charset=utf-8'
            except Exception as e:
                response_parts.append(f"Error loading file: page/{route['show']}")

        response = '\n'.join(response_parts)

        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

# 啟動伺服器
def run():
    server = HTTPServer(('localhost', 8000), NuwaHandler)
    print("Nuwa Web Server is running at http://localhost:8000/")
    server.serve_forever()

if __name__ == '__main__':
    run()