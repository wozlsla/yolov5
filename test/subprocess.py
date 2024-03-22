import subprocess

command = "find ./v1/train/labels -type f -name '*.txt' | wc -l"
output = subprocess.check_output(command, shell=True).decode("utf-8").strip()
print(output)
