url = ["https://www.youtube.com/watch?v=X4uHSpdZSdw", ""]
import json
print(list)
import webbrowser as pygame
import base64
list = base64.b64encode(json.dumps(url))
print(list)
for i in range(4):
    pygame.open_new(base64.b64decode(url))