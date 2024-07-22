import requests
import time


def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN (HTTP Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Down ({type(e).__name__}: {str(e)})"
    
def main():
    url = "http://127.0.0.1"
    status = check_application_status(url)
    print(f"Application status: {status}")

if __name__ == "__main__":
    main()