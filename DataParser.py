class DataParser():
  
  def __init__(self,fileReader,perfData, program):
    self._fileReader = fileReader
    self._perfData = perfData
    self._programName = program
  
  def test(self):
    while self._fileReader.readNextLine():
      print '>>>',self._fileReader.readNextLine()
  
  def parse(self):
    for line in self._fileReader.getFilePointer():
      if 'Samples' in line:
        raw_event = line.split()[6].strip('\'')
        event_count = int(self._fileReader.readNextLine().split()[4])
        
      if '#' not in line and len(line.split())!=0:
        temp = {}
        if line.split()[1] == self._programName:
          size = len(line.split())
          symbol = ''
          overhead = float(line.split()[0].strip('%'))
          shared_obj = line.split()[2]
  
          if size<=5:
            symbol = line.split()[4]
          else:
            i=4
            while(i<size):
              symbol += line.split()[i]
              i+=1
              
          if overhead != 0: interpolated_val = round((event_count/overhead)*100,2)
          else: interpolated_val = '?'
          #print symbol
          temp[raw_event] = interpolated_val
        if len(temp) !=0:
          self._perfData.addValue(symbol, raw_event, interpolated_val)
