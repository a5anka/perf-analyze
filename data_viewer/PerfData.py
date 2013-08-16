#
# This data structure is used to store and access perf data values
# @author: Gayashan Amarasinghe
#
class PerfData():
  
  def __init__(self):
    self._dataStore = {}
  
  def addValue(self, symbol, rawEvent, interpolatedValue):
    if symbol in self._dataStore:
      self._dataStore[symbol][rawEvent] = interpolatedValue
    else:
      self._dataStore[symbol] = {rawEvent:interpolatedValue}
  
  def addRawEventValueCollection(self, symbol, values):
    if symbol in self._dataStore: 
      self._dataStore[symbol] = values
    else:
      raise Exception("Symbol is not a valid key")
    
  def addInterpolatedValue(self, symbol, rawEvent, interpolatedValue):
      self._dataStore[symbol][rawEvent] = interpolatedValue
    
  def getSymbolsList(self):
    return self._dataStore.keys()
  
  def getRawEventValueCollection(self, symbol):
    return self._dataStore[symbol].keys()
  
  def getInterpolatedValue(self, symbol, rawEvent):
    return self._dataStore[symbol][rawEvent]
  
  def getDataStore(self):
    return self._dataStore