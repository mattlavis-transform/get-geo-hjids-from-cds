import os
import csv
import sys
from dotenv import load_dotenv
from .geographical_area import GeographicalArea
from .database import Database


class Loader:
    def __init__(self):
        path = os.getcwd()
        folder = os.path.join(path, "export")
        filename = os.path.join(folder, "hjid_to_sid_map.txt")

        geo_areas = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 1
            for row in csv_reader:
                if line_count > 1:
                    geographical_area_hjid = row[0]
                    geographical_area_sid = row[1]
                    g = GeographicalArea(geographical_area_hjid, geographical_area_sid)
                    geo_areas.append(g)

                line_count += 1

        for geo_area in geo_areas:
            sql = """update public.geographical_areas_oplog set hjid = """ + geo_area.geographical_area_hjid + """ where geographical_area_sid = """ + geo_area.geographical_area_sid
            d = Database()
            d.run_query(sql)
