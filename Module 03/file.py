# .csv -> comma separated value
# .txt -> text file


# with open('message.txt', 'w') as file:
#     file.write('i am writing a new text into the file')


# with open('message.txt', 'a') as file:
#     file.write('i am writing a new text into the file')


with open('message.txt', 'r') as file:
    text = file.read()
    print(text)