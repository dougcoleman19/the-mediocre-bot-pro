import os
import sys
import glob
import sqlite3
from sqlite3 import Error
try:
    CONN = sqlite3.connect('C:/python-dev/mediocre-bot/mediocre.db')
    print('Connected to the database...')
except Error as e:
    print(e)


CURSOR = CONN.cursor()

files = glob.glob('C:/python-dev/5thSRD-master/docs/spellcasting/spells/*.md')

#files = glob.glob('C:/python-dev/5thSRD-master/docs/spellcasting/spells/acid_arrow.md')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.replace('"', '\'')
        data = data.replace("'", "\'")
        #
        spellNameIndex = data.find('name: ')
        spellLevelIndex = data.find('level: ')
        spellSchoolIndex = data.find('school: ')
        spellHashtagIndex = data.find('#')
        spellCastingTimeIndex = data.find('**Casting Time:** ')
        spellRangeIndex = data.find('**Range:** ')
        spellComponentsIndex = data.find('**Components:** ')
        spellBlobIndex = data.find('**Duration:** ')

        spellBlob = data[spellBlobIndex+14:]
        spellBlobSplit = spellBlob.split('\n')
        spellDuration = spellBlobSplit[0]

        spellBody = ''
        for item in spellBlobSplit[1:]:
            spellBody += item + ''
        

        spellName = data[spellNameIndex+6:spellLevelIndex-1]
        spellLevel = data[spellLevelIndex+7:spellSchoolIndex-1]
        spellSchool = data[spellSchoolIndex+8:spellHashtagIndex-2].capitalize()
        spellCastingTime = data[spellCastingTimeIndex+18:spellRangeIndex-1]
        spellRange = data[spellRangeIndex+11:spellComponentsIndex-1]
        spellComponents = data[spellComponentsIndex+16:spellBlobIndex-1]
        #spellDuration = data[]

        query = 'INSERT INTO test (spellName, spellSchool, spellLevel, castingTime, Range, components, duration, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
        
        CONN.execute(query, (spellName, spellSchool, spellLevel, spellCastingTime, spellRange, spellComponents, spellDuration, spellBody))
        CONN.commit()
        

CONN.close()

    #print(spellName)
    #print(spellLevel)
    #print(spellSchool)
    #print(spellCastingTime)
    #print(spellRange)
    #print(spellComponents)
    #print(spellDuration)
    #print(spellBody)