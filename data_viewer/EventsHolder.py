#
# This class holds the list of raw events, and provides access to the events
# @author: Gayashan Amarasinghe
#
class EventsHolder():
  
  def __init__(self, eventsList = [], instructionCount = None):
    self._eventsList = eventsList
    self._instructionCount = instructionCount
    
  def setEventsList(self, eventsList):
    self._eventsList = eventsList
  
  def setInstructionCountRawEvent(self, instructionCountRawEvent=None):
      self._instructionCount = instructionCountRawEvent
    
  def getInstructionCountRawEvent(self):
    if self._instructionCount is None:
      raise Exception('Raw event for instruction count is not set.')
    else:
      return self._instructionCount
  
  def getEventsList(self):
    return self._eventsList
  
  def addRawEvent(self, rawEvent):
    self._instructionCount.append(rawEvent)