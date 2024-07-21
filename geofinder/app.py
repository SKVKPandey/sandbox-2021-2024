from flask import Flask, render_template_string
import socket
import uuid
import requests

app = Flask(__name__)

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 80))  # Use a public DNS server (Google DNS)
        ip_address = s.getsockname()[0]
    except Exception as e:
        ip_address = None
        print(f"Error retrieving IP address: {e}")
    finally:
        s.close()
    
    print(f"Retrieved IP Address: {ip_address}")  # Debugging line
    return ip_address

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    return mac

def get_location(ip_address):
    token = '53a504d27c7bce'  # Replace with your API key
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}?token={token}')
        response.raise_for_status()  # Raise an exception for HTTP errors
        location_data = response.json()
        print(f"API Response: {location_data}")  # Debugging line
    except requests.RequestException as e:
        location_data = {'error': str(e)}
        print(f"Error retrieving location data: {e}")
    
    return location_data

@app.route('/')
def index():
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    location = get_location(ip_address) if ip_address else None

    html = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>System Information</title>
      </head>
      <body>
        <h1>System Information</h1>
        <p><strong>IP Address:</strong> {{ ip_address }}</p>
        <p><strong>MAC Address:</strong> {{ mac_address }}</p>
        <h2>Location Information</h2>
        {% if location %}
          {% if location.error %}
            <p><strong>Error:</strong> {{ location.error }}</p>
          {% else %}
            <p><strong>City:</strong> {{ location.city }}</p>
            <p><strong>Region:</strong> {{ location.region }}</p>
            <p><strong>Country:</strong> {{ location.country }}</p>
            <p><strong>Location:</strong> {{ location.loc }}</p>
          {% endif %}
        {% else %}
          <p>Unable to retrieve location data.</p>
        {% endif %}
      </body>
    </html>
    '''

    return render_template_string(html, ip_address=ip_address, mac_address=mac_address, location=location)

if __name__ == '__main__':
    app.run(debug=True)
