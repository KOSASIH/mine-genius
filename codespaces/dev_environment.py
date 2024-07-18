import os

def create_dev_environment():
    # Create a new Codespace environment
    os.environ["CODESPACE_NAME"] = "mine-genius-dev"
    os.environ["CODESPACE_IMAGE"] = "ubuntu-latest"

if __name__ == "__main__":
    create_dev_environment()
