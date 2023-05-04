import subprocess

# Define the command to be executed
command = "ls "

# Run the command and capture the output
output = subprocess.check_output(command, shell=True)

# Print the output
print("HERE IS THE OUTPUT:")
print(output.decode())
