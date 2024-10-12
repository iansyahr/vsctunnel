from fastnanoid import generate
import subprocess
import os
import time
import re

def install_binary():
    try:
        subprocess.run(["code", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("VSCode CLI is installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("VSCode CLI is not installed")
        print("Install VSCode CLI...")

        os.system("curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz")
        os.system("tar -xf vscode_cli.tar.gz")
        os.environ['PATH'] += ":/content/"
        
        print("Installation process complete.")

def auth_account(provider):
    provider = provider.lower()
    valid_providers = {"microsoft", "github"}
    
    if provider not in valid_providers:
        return "Provider not available"
    
    install_binary()

    command = ["code", "tunnel", "user", "login", "--provider", provider]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    auth_url, auth_code = None, None

    while process.poll() is None:
        for stream in (process.stdout, process.stderr):
            if stream:
                line = stream.readline()
                if not line:
                    continue
                if not auth_url:
                    url_match = re.search(r"(https://[^\s]+)", line)
                    if url_match:
                        auth_url = url_match.group(1)
                        print(f"Authentication URL: {auth_url}")
                if not auth_code:
                    code_match = line.split("code ")
                    if code_match:
                        auth_code = code_match[1]
                        print(f"Authentication Code: {auth_code}")

        if auth_url and auth_code:
            break

    process.wait()

    if auth_url and auth_code:
        return "Login Successful"
    return "Login Failed"

def run(machine_name = None):
    if not machine_name:
        machine_name = generate(size=12)
    subprocess.run(['pkill', 'code'])
    subprocess.run(['rm','vscode-log.txt'])
    with open('vscode-log.txt', 'w') as f:
        subprocess.Popen(['code','tunnel','--name',machine_name], stdout=f, stderr=subprocess.STDOUT)
    return "The VS Code CLI Server has been successfully started. The tunnel link is available in vscode-log.txt"

def kill():
    subprocess.run(['pkill', 'code'])
    return "VS Code has been terminated."