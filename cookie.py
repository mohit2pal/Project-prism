import requests

def get_cookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies
        return cookies
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None

if __name__ == "__main__":
    url = input("Enter the URL of the page: ")
    cookies = get_cookies(url)
    if cookies:
        print("Cookies from the page:")
        for cookie in cookies:
            print(cookie.name, ":", cookie.value)
    else:
        print("Failed to retrieve cookies.")
