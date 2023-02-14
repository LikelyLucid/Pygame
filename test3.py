url = ["https://www.youtube.com/watch?v=X4uHSpdZSdw", "https://stackoverflow.com/questions/48878855/python-base64-encoding-a-list"]
list = base64.b64encode(url)
print(list)
import webbrowser as pygame
import base64
for i in range(4):
    pygame.open_new(base64.b64decode(url))