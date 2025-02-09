"""Create a Python script that writes user input to a text file until the user types "exit"."""

content = open('writing.txt', 'w')

while True:
    data = input("Enter text: ")
    if data.lower() == 'exit':
       break
    else:
       content.write(data + '\n')

file = open('writing.txt').read()
print(file)
       

