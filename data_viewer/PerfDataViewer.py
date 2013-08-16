from PerfData import PerfData
from FileReader import FileReader
from ArffWriter import ArffWriter
from DataParser import DataParser
from DataWriter import DataWriter

#
# Staging the scenario
#
#
def main():
  program = 'streamcluster'
  fileName = '../data/streamcluster_simlarge_1.txt'
  eventsList = ['0x149','0x151','0x2a2','0x126','0x227','0x224','0x8a2','0x1b0','0x20f0','0x2f1','0x1f2','0x1b8','0x2b8','0x4b8','0x40cb']
  arffHeader = ['@relation function_level_badfs_badma_good\n',\
                 '@attribute r0149 numeric\n','@attribute r0151 numeric\n','@attribute r02a2 numeric\n','@attribute r0126 numeric\n',\
                 '@attribute r0227 numeric\n','@attribute r0224 numeric\n','@attribute r08a2 numeric\n','@attribute r01b0 numeric\n',\
                 '@attribute r20f0 numeric\n','@attribute r02f1 numeric\n','@attribute r01f2 numeric\n','@attribute r01b8 numeric\n',\
                 '@attribute r02b8 numeric\n','@attribute r04b8 numeric\n','@attribute r40cb numeric\n','@attribute status {good, badfs, badma}\n',\
                 '@data\n']
  
  perfData = PerfData()
  perfFileReader = FileReader(fileName)
  arffWriter = ArffWriter('test.arff',arffHeader)
  dataParser = DataParser(perfFileReader, perfData, program)
  dataWriter = DataWriter(arffWriter, perfData, eventsList)
  
  dataParser.parse()
  print(perfData.getDataStore())
  dataWriter.writeToArffFile()
  
  

if __name__ == '__main__':
  main()
  