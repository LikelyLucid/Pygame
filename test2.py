# url = ["https://www.youtube.com/watch?v=X4uHSpdZSdw", "https://stackoverflow.com/questions/48878855/python-base64-encoding-a-list"
url = ["aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1YNHVIU3BkWlNkdw==", "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj10T1hvazZHZDQ2UQ==", "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1vOVN6OUQ3ODNXQQ=="]
import webbrowser as pygame
import base64
for url in url):
    pygame.open_new(base64.b64decode(url))