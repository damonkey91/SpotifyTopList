import unittest
import FileReader
import os

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.readFileName = "testReadFilename"
        self.writeFileName = "writeFileName"
        self.readFileNameNotExisting = "readFileNameNotExisting"
        self.writeFileNameNotExisting = "writeFileNameNotExisting"

        self.__removeFileIfExists(self.readFileNameNotExisting)
        self.__removeFileIfExists(self.writeFileNameNotExisting)
        self.__createFileIfNotExist(self.readFileName)
        self.__createFileIfNotExist(self.writeFileName)

    def __removeFileIfExists(self, filename):
            if os.path.exists(filename):
                os.remove(filename)

    def __createFileIfNotExist(self, filename):
        if not os.path.exists(filename):
            open(filename, "w+").close()

    def tearDown(self):
        self.__removeFileIfExists(self.readFileName)
        self.__removeFileIfExists(self.writeFileName)
        self.__removeFileIfExists(self.readFileNameNotExisting)
        self.__removeFileIfExists(self.writeFileNameNotExisting)

    def testReadFileNotExisting(self):
        try:
            FileReader.readFromFile(self.readFileNameNotExisting)
        except FileNotFoundError:
            return
        self.assertFalse(True)

    def testReadFileThatExists(self):
        readText = FileReader.readFromFile(self.readFileName)
        self.assertIsNotNone(readText)

    def testWriteToFileThatDoesNotExist(self):
        FileReader.writeToFile(self.writeFileNameNotExisting, "Testtest")

    def testWriteToExistingFile(self):
        FileReader.writeToFile(self.writeFileName, "Testtest2")

