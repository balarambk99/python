import os

# Define the file name
file_name = "jenkins_test.txt"

# 1. Write content to a file
print(f"--- Creating file: {file_name} ---")
with open(file_name, "w") as f:
    f.write("Hello! This file was created by Python inside Jenkins.\n")
    f.write("Build test: SUCCESSFUL\n")
print("hello freinds wellcome to jenkins")
print("This file has been created and written to successfully.")

# 2. Read the content back
print(f"--- Reading content from: {file_name} ---")
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        print(f.read())
else:
    print("Error: File was not created.")

# 3. Clean up (Optional - uncomment the line below to delete the file after reading)
# os.remove(file_name)
