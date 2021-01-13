# Get geographical area and membership hjids values from CDS data extract

## Introduction

In order to allow for data from the CDS export (in future CDS format) to be incorporated successfully into the database, we need to utlise the hjid fields in the datasets produced from CDS, even though these are not Taric-3 compliant fields.

The way to do this is to do the following:

- Take the full extract of data from CDS that is due to be produced on Jan 2nd (TBC)

- Download a copy of this full data set (in CDS format)

- Run this Python script to create a full list of all of the hjids associated with these two data objects

## Caveat

The CDS file is huge, and while it is possible to write some SAX to run through the file to retrieve the right data, the benefit of the CDS format is arranged in such a way that all of the geographical areas are in one place in the XML extract, between these two nodes:

`<findGeographicalAreaByDatesResponse>`

`...`

`</findGeographicalAreaByDatesResponse>`

## Steps

- Take the source file (8-10 Gb)
- Trim it at the nodes noted above (inclusive) + add the surrounding root nodes etc.
- Run the Python against the resulting file, which will be closer to 5Mb in size and therefore manageable in the more standard way, using lxml with no SAX components.

`python3 parse.py`

## What it does

- Runs through every instance of GeographicalArea tag
  - Stores the hjid against the geographical_area_sid
  - Stores full list in hjid_to_sid_map.txt
- Runs through every instance of geographicalAreaMembership tag
  - Stores the hjid against the geographical_area_sid for both parent and child
  - Stores full list in hjid_member_map.txt