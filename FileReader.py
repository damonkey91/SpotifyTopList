import LoggerWrapper

def readFromFile(fileName):
    with open(fileName, 'r') as file:
        readLines = file.readlines()
        return readLines

def writeToFile(fileName, textToWrite):
    with open(fileName, 'w') as file:
        file.write(textToWrite)




def readLinesFromFile(filePath, startLine, endLine):
    savedLines =[]
    totalLinesToRead = endLine - startLine
    isStartLineGreaterThanEndLine = endLine > startLine
    currentLineCounter = 1
    with open(filePath) as reader:
        line = reader.readline()
        while line != '':
            print(line, end='')
            line = reader.readline()
            if currentLineCounter >= startLine and currentLineCounter <= currentLineCounter:
                savedLines.append(line)
            if currentLineCounter > endLine:
                break
            currentLineCounter += 1

