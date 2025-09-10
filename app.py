from flask import Flask, Response
import random
import string

app = Flask(__name__)

# Function to generate random HTML content of specified size (in bytes)
def generate_html_content(target_size_bytes):
    # Basic HTML structure size estimate
    base_html = "<!DOCTYPE html><html><head><title>Test HTML</title></head><body>{}</body></html>"
    # Estimate for random content (assuming ASCII characters)
    content_size = target_size_bytes - len(base_html.format(""))
    # Generate random string for content
    random_content = ''.join(random.choices(string.ascii_letters + ' ', k=content_size))
    # Format HTML with random content
    html_content = base_html.format(random_content)
    return html_content

@app.route('/html/<size>')
def serve_html(size):
    size_map = {
        '10kb': 10 * 1024,
        '100kb': 100 * 1024,
        '1mb': 1024 * 1024,
        '5mb': 5 * 1024 * 1024,
        '10mb': 10 * 1024 * 1024
    }
    
    target_size = size_map.get(size.lower())
    if not target_size:
        return Response("Invalid size. Use 10kb, 100kb, 1mb, 5mb, or 10mb.", status=400)
    
    html_content = generate_html_content(target_size)
    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)