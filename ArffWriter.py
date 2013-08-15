class ArffWriter():
  _write_flag = 'wb'
  
  def __init__(self, fileName, headers):
    self._fileName = fileName
    self._filePointer = self.open()
    self._headers = headers
    self._filePointer.writelines(headers)
    
  def open(self):
    return open(self._fileName, 'wb')
  
  def write(self, stringToWrite):
    self._filePointer.write(stringToWrite)
    
  def writeLines(self,stringSequenceToWrite):
    self._filePointer.writelines(stringSequenceToWrite)