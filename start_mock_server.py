import subprocess
import time

def start_mock():
    # Executa o mock em background
    process = subprocess.Popen(['python', 'mock_server.py'])
    time.sleep(2)  # Espera o servidor subir
    with open("mock_pid.txt", "w") as f:
        f.write(str(process.pid))

if __name__ == "__main__":
    start_mock()
