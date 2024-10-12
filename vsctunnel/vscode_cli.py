import subprocess
import os
import time

def install_binary():
    try:
        subprocess.run(["code", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("VSCode CLI sudah terinstall.")
    except subprocess.CalledProcessError:
        print("VSCode CLI belum terinstall")
        print("Kami menginstall programnya terlebih dahulu")

        os.system("curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz")
        os.system("tar -xf vscode_cli.tar.gz")
        os.environ['PATH'] += ":/content/"
        
        print("Proses Instalasi selesai")

def select_account(account_name):
    install_binary()

    process = subprocess.Popen(
        ["code", "tunnel"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            if account_name in output:
                process.stdin.write(f"{account_name}\n")
                process.stdin.flush()
                time.sleep(0.5)

    final_output, _ = process.communicate()
    return final_output