with open('../Resources/test.txt','r') as reader:
    content = reader.readlines()
    reversedContent = reversed(content)
 #   content.reverse()
 #   print(content)
    with open('../Resources/output.txt', 'w') as writer:
        for line in reversedContent:
            writer.write(line)