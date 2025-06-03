import os
import signal

def stop_mock():
    try:
        with open("mock_pid.txt", "r") as f:
            pid = int(f.read())
        os.kill(pid, signal.SIGTERM)
        print("Mock finalizado.")
    except Exception as e:
        print(f"Erro ao parar o mock: {e}")

if __name__ == "__main__":
    stop_mock()
