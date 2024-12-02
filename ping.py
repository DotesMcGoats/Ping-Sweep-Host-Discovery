import subprocess

def ping(host):
    try:
        for i in host:
            output = subprocess.check_output(
                ["ping", "-c", "1", i], universal_newlines=True
            )
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}"