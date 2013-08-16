# File Reader class
#
# Read a given file and provide access to the file
# @author: Gayashan Amarasinghe
#
class FileReader():
  _read_flag = 'rb'
  
  def __init__(self, fileName):
    self._fileName = fileName
    self._filePointer = self.open()
    
  def open(self):
    return open(self._fileName, 'rb')
  
  def getFilePointer(self):
    return self._filePointer
  
  def readLine(self):
    return self._filePointer.readline()
  
  def readLines(self):
    return self._filePointer.readlines()
  
  def readNextLine(self):
    return self._filePointer.next()
