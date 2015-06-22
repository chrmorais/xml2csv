from xml.dom import minidom
import os
import csv


def xmlParser(fname, csvWriter):
    doc = minidom.parse(fname)

    newLine = []
    names = ''
    
    awardID = doc.getElementsByTagName("AwardID")[0]
    newLine.append(awardID.firstChild.data)
    
    title = doc.getElementsByTagName("AwardTitle")[0]
    newLine.append(title.firstChild.data)
    
    startDate = doc.getElementsByTagName("AwardEffectiveDate")[0]
    newLine.append(startDate.firstChild.data)
    
    endDate = doc.getElementsByTagName("AwardExpirationDate")[0]
    newLine.append(endDate.firstChild.data)
    
    award = doc.getElementsByTagName("AwardAmount")[0]
    newLine.append(award.firstChild.data)

    awardTypes = doc.getElementsByTagName("AwardInstrument")
    for awardType in awardTypes:
        newLine.append(awardType.getElementsByTagName("Value")[0].firstChild.data)

    investigators = doc.getElementsByTagName("Investigator")
    for investigator in investigators:
       firstName = investigator.getElementsByTagName("FirstName")[0].firstChild.data
       lastName = investigator.getElementsByTagName("LastName")[0].firstChild.data
       names = names + firstName + ' ' + lastName + ';'
    newLine.append(names)
        
    institutions = doc.getElementsByTagName("Institution")
    for institution in institutions:
        university = institution.getElementsByTagName("Name")[0].firstChild.data
    newLine.append(university)

    #print newLine
    csvWriter.writerow(newLine)
    #csvWriter.writerow(newLine)

def directorySearcher(csvWriter):
    wd = os.getcwd() + '/NSF_awards_2014'
    
    for f in os.listdir(wd):
        fname = wd + '/'+ f
        xmlParser(fname, csvWriter)

def main():
    with open('data.csv', 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter = ',')

        directorySearcher(csvWriter)

main()

