import requests
import time

def measure_response_time(url, num_requests=100):
    response_times = []

    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            response_times.append(end_time - start_time)
        else:
            print(f"Request failed with status code {response.status_code}")

    if response_times:
        average_response_time = sum(response_times) / len(response_times)
        print(f"Average response time over {num_requests} requests: {average_response_time:.4f} seconds")
    else:
        print("No successful requests to measure.")

# Example usage
api_url = "https://api-web.nhle.com/v1/gamecenter/1982020194/play-by-play"
measure_response_time(api_url, num_requests=100)