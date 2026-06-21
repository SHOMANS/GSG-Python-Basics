import subprocess
import sys

# Write to a file
# with open("file.txt", "w") as f:
#     f.write("Hello")

# Read from a file
# with open("file.txt", "r") as f:
#     print(f.read())

# # Append to a file
# with open("file.txt", "a") as f:
#     f.write("\nNew line again")


# with open("file.csv", "w") as f:
#     f.write("name,age\nfatma,20\nahmed,25")

names = ["ahmed", "mohammed", "eman", "mahmoud", "saja"]
for i in range(len(names)):
    with open(f"script{i}.py", "w") as f:
        f.write(f"print('hello {names[i]}')")

    # Runs script.py using the current Python interpreter
    subprocess.run([sys.executable, f"script{i}.py"])

# message = ""

# with open("file.txt", "r") as f:
#     print(f.read())

# newMessage = message.replace("Jeneen", "Nour")
# print(newMessage)

# with open("file.txt", "w") as f:
#     f.write(newMessage)
