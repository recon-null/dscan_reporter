# This file is part of DScan Reporter.
#
# DScan Reporter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DScan Reporter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DScan Reporter.  If not, see <http://www.gnu.org/licenses/>.


# CSV parser
import csv

def main():

    # Open the summary file
    reader = csv.reader(open('ships.csv', 'r'))
    ships = open("ships.txt", 'w')
    shipNames = open("ship_names.txt", 'w')
    shipTypes = open("ship_types.txt", 'w')
    shipClasses = open("ship_classes.txt", 'w')
    
    shipNamesDict = {}
    shipTypesDict = {}
    shipClassesDict = {}
    shipsDict = {}

    # Go through all the ships
    for row in reader:
        if (not shipTypesDict.has_key(row[1])):
            shipTypesDict[row[1]] = 1;
        if (not shipClassesDict.has_key(row[2])):
            shipClassesDict[row[2]] = 1;
        shipsDict[row[0]] =  [row[1], row[2]];
        shipNamesDict[row[0]] = 1
        

    shipNames.write('$shipNames = array(')
    for shipName in shipNamesDict:
        shipNames.write('\'')
        shipNames.write(shipName)
        shipNames.write('\' => 0, ')     
    shipNames.write(');')

    shipTypes.write('$shipTypes = array(')
    for shipType in shipTypesDict:
        shipTypes.write('\'')
        shipTypes.write(shipType)
        shipTypes.write('\' => 0, ')    
    shipTypes.write(');')

    shipClasses.write('$shipClasses = array(')
    for shipClass in shipClassesDict:
        shipClasses.write('\'')
        shipClasses.write(shipClass)
        shipClasses.write('\' => 0, ')    
    shipClasses.write(');')

    shipTemplate = "'{0}' => array('{1}', '{2}')"

    ships.write('$ships = array(')
    for ship, info in shipsDict.iteritems():        
        ships.write(shipTemplate.format(ship, info[0], info[1]))
        ships.write(', ')    
    ships.write(');')

if __name__ == '__main__':
    main()
