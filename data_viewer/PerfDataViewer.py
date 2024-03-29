from PerfData import PerfData
from FileReader import FileReader
from ArffWriter import ArffWriter
from DataParser import DataParser
from DataWriter import DataWriter
from EventsHolder import EventsHolder
import sys
#
# Staging the scenario
#
#
def main():
  if len(sys.argv) != 4:
    print 'Missing file operands!'
    print 'PerfDataViewer.py [program] [input_data_file] [output_data_file]'
    return

  program = str(sys.argv[1])
  inFileName = str(sys.argv[2])
  outFileName = str(sys.argv[3])
  
  #TODO: move these to configuration files
  eventsList = ['0x149','0x151','0x2a2','0x126','0x227','0x224','0x8a2','0x1b0','0x20f0','0x2f1','0x1f2','0x1b8','0x2b8','0x4b8','0x40cb']
  ppc_eventsList = ['0x3c046','0x2c048','0x2f080','0x26080','0x30881','0x26182','0x26880','0xd0a2','0xd0a0']
  arffHeader = ['@relation function_level_badfs_badma_good\n',\
                 '@attribute r0149 numeric\n','@attribute r0151 numeric\n','@attribute r02a2 numeric\n','@attribute r0126 numeric\n',\
                 '@attribute r0227 numeric\n','@attribute r0224 numeric\n','@attribute r08a2 numeric\n','@attribute r01b0 numeric\n',\
                 '@attribute r20f0 numeric\n','@attribute r02f1 numeric\n','@attribute r01f2 numeric\n','@attribute r01b8 numeric\n',\
                 '@attribute r02b8 numeric\n','@attribute r04b8 numeric\n','@attribute r40cb numeric\n','@attribute status {good, badfs, badma}\n',\
                 '@data\n']
  
  ppc_arffHeader = ['@relation function_level_badfs_badma_good\n',\
                    '@attribute r3c046 numeric\n', '@attribute r2c048 numeric\n', '@attribute r2f080 numeric\n',\
                    '@attribute r26080 numeric\n', '@attribute r30881 numeric\n', '@attribute r26182 numeric\n',\
                    '@attribute r26880 numeric\n', '@attribute rd0a2 numeric\n', '@attribute rd0a0 numeric\n',\
                    '@attribute status {good, badfs, badma}\n', '@data\n']
  
  perfData = PerfData()
  
  perfFileReader = FileReader(inFileName)
  dataParser = DataParser(perfFileReader, perfData, program)
  
  eventsHolder = EventsHolder(eventsList)
  eventsHolder.setInstructionCountRawEvent('0xc0')
  
  arffWriter = ArffWriter(outFileName,arffHeader)
  dataWriter = DataWriter(arffWriter, perfData, eventsHolder)
  
  dataParser.parse()
  print(perfData.getDataStore())
  dataWriter.writeToArffFile()

  print outFileName + ' file was created successfully.'

if __name__ == '__main__':
  main()

