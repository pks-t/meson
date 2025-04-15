import subprocess
import sys

output = subprocess.check_output([sys.argv[1]], encoding='utf-8')
if output != sys.argv[2]:
    sys.exit(f'expected and actual output do not match: "{output}" != {sys.argv[2]}')
