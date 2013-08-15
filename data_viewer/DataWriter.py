class DataWriter():
  
  def __init__(self, arffWriter, perfData, eventsList):
    self._arffWriter = arffWriter
    self._perfData = perfData
    self._eventsList = eventsList
    
  def writeToArffFile(self):
    i=1
    for symbol in self._perfData.getSymbolsList():
      for event in self._eventsList:
        if event not in self._perfData.getRawEventValueCollection(symbol):
          self._perfData.addInterpolatedValue(symbol,event,'?')
      
      #write to the arff file only if instruction count [0xc0] is available for the function
      if '0xc0' in self._perfData.getRawEventValueCollection(symbol) and self._perfData.getInterpolatedValue(symbol,'0xc0') != '?':     
      #write to the output arff file
        out = ''
        self._arffWriter.write('%\n'+'% '+str(i)+' Function: '+symbol+'\n%\n')
        i += 1
        #print 'Function: '+symbol
        for event in self._eventsList:
          if self._perfData.getInterpolatedValue(symbol, event) == '?':
            out += str(self._perfData.getInterpolatedValue(symbol, event)) + ','
          else:
            out += str(self._perfData.getInterpolatedValue(symbol, event)/self._perfData.getInterpolatedValue(symbol, '0xc0')*pow(10, 9)) + ','
        out += '?\n'
        #print out
        self._arffWriter.write(out)
    