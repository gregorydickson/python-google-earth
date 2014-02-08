import csv
import xml.dom.minidom
import sys
import fileinput

def convertDegreesMinSecToDecimal(coordinate):
  # takes a "degrees-minutes-seconds" format and converts to decimal
  # assumes the use of a "-" as the delimiter
  # formula for conversion is Degrees+(minutes/60)+(seconds/3600)
  # is the coordinate negative?
  #print "Coordinate = " + coordinate
  negative = 0
  if coordinate[0] == "-":
    negative = 1
    coordinate = coordinate.lstrip('-')
  # split apart the degrees, minutes, seconds into a list
  listOfDegreesMinutesSeconds = coordinate.split('-')
  # get degrees
  convertedCoordinate = float(listOfDegreesMinutesSeconds[0])
  # get minutes
  convertedCoordinate = convertedCoordinate + (float(listOfDegreesMinutesSeconds[1])/60)
  # get seconds 
  convertedCoordinate = convertedCoordinate + (float(listOfDegreesMinutesSeconds[2])/3600)
  if negative:
    convertedCoordinate = convertedCoordinate * -1
  #print "converted Coordinate is " + str(convertedCoordinate)
  return convertedCoordinate



def createNewFile(csvReader):
  # This constructs the new csv file.
  csvWriter = csv.writer(open('testdata.csv', 'w'), delimiter=',')
  # Skip the header line.
  csvReader.next()
  for row in csvReader:
    latitude = convertDegreesMinSecToDecimal(row['Lat'])
    longitude = convertDegreesMinSecToDecimal(row['Long'])
    csvWriter.writerow([latitude, longitude, row['Driverid']])
    
 

def main():
  # This reader opens up 'driverlocations.csv', 
  # It creates a new csv file called 'testdata.csv'.
  # 
  order = ['Lat', 'Long', 'Driverid']
  print "new world order is " + str(order)
  fileDelimiter = ","
  csvreader = csv.DictReader(open('driverlocations.csv'),order,delimiter = fileDelimiter)
  createNewFile(csvreader)
if __name__ == '__main__':
  main()