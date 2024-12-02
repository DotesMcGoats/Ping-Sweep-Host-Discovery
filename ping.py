import subprocess


def ping(host):
    output = []
    try:
        for i in host:
            print(f"Pinging {i}")
            output = subprocess.check_output(
                ["ping", "-c", "1", i], universal_newlines=True
            )
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}"
