# Using 'with' statement to close files automatically
with open('sample.txt', 'r') as f:
    content = f.read()
    print(content)