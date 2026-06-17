import random
import time
import concurrent.futures

SERVERS = [
    {"ip": "10.0.0.1", "service": "auth-api"},
    {"ip": "10.0.0.2", "service": "payment-gateway"},
    {"ip": "10.0.0.3", "service": "database-primary"},
    {"ip": "10.0.0.4", "service": "redis-cache"},
    {"ip": "10.0.0.5", "service": "frontend-lb"},
    {"ip": "10.0.0.6", "service": "logging-agent"},
    {"ip": "10.0.0.7", "service": "notification-svc"},
    {"ip": "10.0.0.8", "service": "analytics-db"}
]

def random_latency(server):
    ip = server["ip"]
    service = server["service"]
    latency = random.uniform(1,2)
    time.sleep(latency)
    status = "HEALTHY" if random.random() > 0.2 else "CRITICAL"
    return f"[ Metrics ] Service: {service} IP: {ip} Status: {status} Latency: {latency}"


def main():
    print(f"Starting health checks on {len(SERVERS)} infrastructure targets...")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(random_latency,SERVERS)
        for result in results:
            print(result)

    total_time = time.time()-start_time
    print(f"\n Ops completed in {total_time} seconds")


if __name__ == '__main__':
    main()