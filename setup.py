import os
import subprocess
import sys

def create_virtualenv():
    if not os.path.exists('.venv'):
        subprocess.check_call([sys.executable, '-m', 'venv', '.venv'])

def install_requirements():
    activate_script = os.path.join('.venv', 'bin', 'activate_this.py')
    with open(activate_script) as f:
        exec(f.read(), dict(__file__=activate_script))

    subprocess.check_call([os.path.join('.venv', 'bin', 'pip'), 'install', '-r', 'requirements/base.txt'])

if __name__ == '__main__':
    create_virtualenv()
    install_requirements()
    print("\n\nRun 'source .venv/bin/activate' to activate the virtual environment.")
