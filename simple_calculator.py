from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class CalculatorServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple Calculator</title>
        </head>
        <body>
            <h1>Simple Calculator</h1>
            <form action="/" method="get">
                <input type="text" name="num1" placeholder="First Number" required>
                <input type="text" name="num2" placeholder="Second Number" required>
                <select name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select>
                <button type="submit">Calculate</button>
            </form>
        '''

        if self.path.startswith('/?'):
            query = urlparse.urlparse(self.path).query
            params = urlparse.parse_qs(query)

            try:
                num1 = float(params['num1'][0])
                num2 = float(params['num2'][0])
                operation = params['operation'][0]

                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    result = num1 / num2 if num2 != 0 else "Error! Division by zero."
                else:
                    result = "Invalid operation"

                html_content += f'<h2>Result: {result}</h2>'
            except Exception as e:
                html_content += f'<h2>Error: {str(e)}</h2>'

        html_content += '''
        </body>
        </html>
        '''
        self.wfile.write(bytes(html_content, "utf8"))

def run(server_class=HTTPServer, handler_class=CalculatorServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
