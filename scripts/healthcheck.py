import requests

response = requests.post(
    url='http://localhost:443/translate',
    headers={'Content-Type': 'application/json'},
    json={
         'q': 'Hello World!',
         'source': 'en',
         'target': 'en'
    },
    timeout=60
)
# if server unavailable then requests with raise exception and healthcheck will fail
