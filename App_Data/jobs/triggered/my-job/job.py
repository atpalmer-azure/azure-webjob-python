import requests


URL = 'https://www.google.com/'


def main():
    response = requests.get(URL)
    print("Status", response.status_code)


if __name__ == "__main__":
    main()
