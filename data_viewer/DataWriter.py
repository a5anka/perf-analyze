#
# This class is used to handle the writing parsed perf data to the arff file
# @author: Gayashan Amarasinghe
#
class DataWriter():
  
  def __init__(self, ouputWriter, perfData, eventsHolder):
    self._outputWriter = ouputWriter
    self._perfData = perfData
    self._eventsHolder = eventsHolder
  
  #
  # Write the perfData values to the arff file
  #
  def writeToArffFile(self):
    i=1
    for symbol in self._perfData.getSymbolsList():
      for event in self._eventsHolder.getEventsList():
        if event not in self._perfData.getRawEventValueCollection(symbol):
          self._perfData.addInterpolatedValue(symbol,event,'?')
      
      #write to the arff file only if instruction count [0xc0] is available for the function
      if self._eventsHolder.getInstructionCountRawEvent() in self._perfData.getRawEventValueCollection(symbol)\
       and self._perfData.getInterpolatedValue(symbol,self._eventsHolder.getInstructionCountRawEvent()) != '?':     
      #write to the output arff file
        out = ''
        self._outputWriter.write('%\n'+'% '+str(i)+' Function: '+symbol+'\n%\n')
        i += 1
        #print 'Function: '+symbol
        for event in self._eventsHolder.getEventsList():
          if self._perfData.getInterpolatedValue(symbol, event) == '?':
            out += str(self._perfData.getInterpolatedValue(symbol, event)) + ','
          else:
            out += str(self._perfData.getInterpolatedValue(symbol, event)/self._perfData.getInterpolatedValue(symbol, self._eventsHolder.getInstructionCountRawEvent())*pow(10, 9)) + ','
        out += '?\n'
        #print out
        self._outputWriter.write(out)
  
  #
  # Used to change the output writer in runtime
  #       
  def setOutputWriter(self, outputWriter):
    self._outputWriter = outputWriter
  
  #
  # Used to set the events list
  #
  def setEventsHolder(self, eventsHolder):
    self._eventsHolder = eventsHolder
    