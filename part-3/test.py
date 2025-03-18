import threading
import requests
import time

def make_request(client_id):
    print(f"Client {client_id}: Starting request")
    try:
        start_time = time.time()
        response = requests.get('http://localhost:5000/HelloWorld.html')
        elapsed = time.time() - start_time
        
        print(f"Client {client_id}: Status {response.status_code}, Time: {elapsed:.2f}s")
        if response.status_code == 200:
            print(f"Client {client_id}: Response length: {len(response.text)} chars")
        else:
            print(f"Client {client_id}: Error response: {response.text[:100]}")
    except Exception as e:
        print(f"Client {client_id}: Exception: {e}")

num_clients = 5
threads = []

for i in range(num_clients):
    t = threading.Thread(target=make_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All client requests completed")