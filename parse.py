from lxml import etree
import xml.etree.ElementTree as ET
import os
import sys
import csv
from geographical_area import GeographicalArea


def parseXML(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    cwd = os.getcwd()
    output_folder = os.path.join(cwd, "export")
    geo_file = os.path.join(output_folder, "hjid_to_sid_map.txt")
    geo_member_file = os.path.join(output_folder, "hjid_member_map.txt")

    f = open(geo_file, "w+")
    f2 = open(geo_member_file, "w+")
    f.write('"geographical_area_hjid","geographical_area_sid"\n')
    f2.write('"geographical_area_membership_hjid","geographical_area_hjid","geographical_area_sid","geographical_area_group_hjid","geographical_area_group_sid"\n')

    # Get the hjids for the geographical areas
    for geo in root.findall('.//GeographicalArea'):
        hjid = geo.find("hjid").text
        sid = geo.find("sid").text
        # On first pass, just write the HJIDs for the geo areas themselves
        f.write(str(hjid) + "," + str(sid) + "\n")

    f.close()

    # Once the first pass has been through, load all of the CSV data back in
    geographical_areas = []
    with open(geo_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                ga = GeographicalArea()
                ga.hjid = row[0]
                ga.sid = row[1]
                geographical_areas.append(ga)
                line_count += 1
        print(f'Processed {line_count} lines.')

    print (len(geographical_areas))



    # Get the hjids for the geographical areas
    for geo in root.findall('.//GeographicalArea'):
        hjid = geo.find("hjid").text
        sid = geo.find("sid").text

        # Get the hjids for the geographical area memberships
        for member in geo.findall('geographicalAreaMembership'):
            geographical_area_membership_hjid = member.find("hjid").text
            geographical_area_hjid = member.find("geographicalAreaGroupSid").text
            # On second pass, do not (rewrite) the geo data, but look up the hjid in the previously written CSV
            geographical_area_sid = "NOT FOUND"
            for ga in geographical_areas:
                if geographical_area_hjid == ga.hjid:
                    geographical_area_sid = ga.sid

            f2.write(str(geographical_area_membership_hjid) + "," + str(geographical_area_hjid) + "," + str(geographical_area_sid) + "," + str(hjid)  + "," + str(sid) + "\n")

    # Close the files
    f2.close()

if __name__ == "__main__":
    filename = "cds_partsab.xml"
    filename = os.path.join("import", filename)
    parseXML(filename)
