url = ["https://www.youtube.com/watch?v=X4uHSpdZSdw", ""
url = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1YNHVIU3BkWlNkdw=="
import webbrowser as pygame
import base64
for i in range(4):
    pygame.open_new(base64.b64decode(url))