# Create a database called tracks.db
# Create 3 tables:
#    1. Artist (id, name)
#    2. Album (id, artist_id, title)
#    3. Track (id, title, album_id, track_duration_in_seconds, rating, play_count)
# Study the file "Library.xml". Look at how the data is structured.
# For each track that occurs in the file, insert records into the Artist, Album and Track tables.
# If the Artist already exists, or if the Album already exists, then you should not insert a new entry in those tables.
# Make sure that the "id" fields are primary keys with auto-increment.

i = 0

import sqlite3 as sql
import xml.etree.ElementTree as ET
from platform import node

# Setting up the cursor
conn = sql.connect("tracks.db")
csr = conn.cursor()

# Creating the tables
csr.execute("DROP TABLE IF EXISTS Artist")
csr.execute("CREATE TABLE Artist (name varchar(64), id int)")
csr.execute("DROP TABLE IF EXISTS Album")
csr.execute("CREATE TABLE Album (id int, artist_id int)")
csr.execute("DROP TABLE IF EXISTS Track")
csr.execute("CREATE TABLE Track (id int, title varchar(64), album_id int, track_duration_in_seconds, rating int, play_count int)")

# Reading data
tree = ET.parse("Library.xml")
root = tree.getroot()

# Extracting data from root

trackIds = list()
albums = list()
artists = list()

for node in root:
    nodeDict = node[17]
for item in nodeDict:
    trackInfo = nodeDict[3]
    trackIds.append((nodeDict[i].text))
    albums.append(trackInfo[3])
    artists.append(trackInfo[1])
    i += 1
i = 0


