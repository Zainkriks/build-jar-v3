import json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")


f = open("./README.md", "w")

f.write(f'''
   
#### This Page Create at:

```bash

{timestr}

```

#### Create By Machine:

```bash

Host Name : {socket.gethostname()}

platform  : {platform.platform()}

Ip Local  : {socket.gethostbyname(socket.gethostname())}

```

''')

f.close()