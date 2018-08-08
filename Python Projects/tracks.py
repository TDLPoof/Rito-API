# Create a database called tracks.db
# Create 3 tables:
#    1. Artist (id, name)
#    2. Album (id, artist_id, title)
#    3. Track (id, title, album_id, track_duration_in_seconds, rating, play_count)
# Study the file "Library.xml". Look at how the data is structured.
# For each track that occurs in the file, insert records into the Artist, Album and Track tables.
# If the Artist already exists, or if the Album already exists, then you should not insert a new entry in those tables.
# Make sure that the "id" fields are primary keys with auto-increment.



import sqlite3 as sql
import xml.etree.ElementTree as ET
from platform import node



conn = sql.connect("tracks.db")
csr = conn.cursor()

csr.execute("DROP TABLE IF EXISTS Artist")
csr.execute("CREATE TABLE Artist (name varchar(64), id INTEGER PRIMARY KEY AUTOINCREMENT)")
csr.execute("DROP TABLE IF EXISTS Album")
csr.execute("CREATE TABLE Album (id INTEGER PRIMARY KEY AUTOINCREMENT, artist_id int , title varchar(64))")
csr.execute("DROP TABLE IF EXISTS Track")
csr.execute("CREATE TABLE Track (id INTEGER PRIMARY KEY, title varchar(64), album_id int, track_duration_in_seconds, rating int, play_count int)")

tree = ET.parse("Library.xml")
root = tree.getroot()

def getValue(node, keyname):
    i = -1
    found = False
    children = node.getchildren()
    for child in children:
        i += 1
        if(child.tag == "key" and child.text == keyname):
            found = True
            break
    if found:
        return children[i + 1].text

# Check if "name" exists in the artist table
# If yes, then return the corresponding artist id
# If not, then insert an entry with that artist name into the artist table, and return the id.
def getArtistID(name):
    csr.execute("SELECT * FROM Artist WHERE name = '%s')" % (name))

# Similar to getArtistID
def getAlbumID(title):
    csr.execute("SELECT * FROM Album WHERE title = '%s')" % (title))

trackElements = root.findall("dict/dict/dict")

for node in trackElements:
    trackId = getValue(node, "Track ID")
    trackName = getValue(node, "Name")
    albumName = getValue(node, "Album")
    artist = getValue(node, "Artist")
    trackDuration = getValue(node, "Total Time")
    trackRating = getValue(node, "Rating")
    trackPlayCount = getValue(node, "Play Count")
    insertQueryII = "INSERT INTO Artist (name) VALUES('%s')" % (artist)
    csr.execute(insertQueryII)
    
conn.commit()
conn.close()
# DO NOT FORGET TO COMMIT and CLOSE    