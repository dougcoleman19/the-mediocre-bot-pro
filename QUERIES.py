import discord
from discord import Embed, Color
import urllib
import sqlite3
from sqlite3 import Error
from time import gmtime, strftime
import sys
import random

DB_FILE = 'mediocre.db'
CONN = sqlite3.connect('mediocre.db')
CURSOR = CONN.cursor()

def create_connection(DB_FILE):
    try:
        CONN = sqlite3.connect(DB_FILE)
        print('Connected to the database...')
        return CONN
    except Error as e:
        print(e)

    return None


def get_pun():
    create_connection(DB_FILE)
    curr = CONN.cursor()

    isImage = 0

    curr.execute("SELECT COUNT(*) FROM puns")
    rows = curr.fetchall()

    count = rows[0][0]

    punID = random.randint(1,int(count))

    rows = []

    query = 'SELECT pun FROM puns WHERE id = {0}'.format(punID)

    curr.execute(query)
    rows = curr.fetchall()

    pun = rows[0][0]

    if "img:" in pun:
        header, sep, imageLoc = pun.partition(':')
        isImage = 1
        pun = imageLoc

    return pun, isImage

def get_spell_list():
    create_connection(DB_FILE)
    curr = CONN.cursor()

    
    curr.execute('SELECT id, spellName FROM spells')
    rows = curr.fetchall()

    return rows

def get_spell_list_by_school_level(school,level):
    create_connection(DB_FILE)
    curr = CONN.cursor()

    query = 'SELECT id, spellName FROM spells WHERE spellSchool = \'{0}\' AND spellLevel = \'{1}\';'.format(school,level)

    curr.execute(query)
    rows = curr.fetchall()

    return rows

def get_spell_by_id(spellID):
    create_connection(DB_FILE)
    curr = CONN.cursor()

    #query = 'SELECT spells.spellName, spells.spellSchool, spells.spellLevel, spells.castingTime, spells.Range, spells.components, spells.duration, spells.description, spells.pageNumber, books.bookTitle, GROUP_CONCAT(classes.className, ", ") AS Classes FROM spells INNER JOIN books ON spells.book_id = books.id INNER JOIN spell_class ON spells.id = spell_class.spellID INNER JOIN classes on spell_class.classID = classes.id WHERE spells.id = {0}'.format(spellID)
    query = 'SELECT spells.spellName, spells.spellSchool, spells.spellLevel, spells.castingTime, spells.Range, spells.components, spells.duration, spells.description, books.bookTitle, spells.pageNumber FROM spells INNER JOIN books ON spells.book_id = books.id WHERE spells.id = \'{0}\''.format(spellID)
    curr.execute(query)
    rows = curr.fetchall()

    return rows

def get_quote():
    create_connection(DB_FILE)
    curr = CONN.cursor()

    curr.execute("SELECT COUNT(*) FROM quotes")
    rows = curr.fetchall()

    count = rows[0][0]

    quoteID = random.randint(1,int(count))

    rows = []

    query = 'SELECT quote, submitted_by, date FROM quotes WHERE id = {0}'.format(quoteID)

    curr.execute(query)
    rows = curr.fetchall()

    quote = rows[0][0]
    author = rows[0][1]
    date = rows[0][2]

    return quote, author, date


def add_quote(quote, author, date):
    create_connection(DB_FILE)
    curr = CONN.cursor()

    query = "INSERT INTO quotes (quote, submitted_by, date) VALUES (\"{0}\", \"{1}\", \"{2}\");".format(quote, author, date)

    curr.execute(query)
    CONN.commit()

    return None


def get_feats():
    create_connection(DB_FILE)
    curr = CONN.cursor()

    query = 'SELECT feats.title, feats.prerequisite_skill, feats.prerequisite_level, feats.description, books.bookTitle FROM feats INNER JOIN books ON feats.bookID = books.id '

    curr.execute(query)
    rows = curr.fetchall()

    feat = rows[0][0]
    skill = rows[0][1]
    level = rows[0][2]
    description = rows[0][3]
    source = rows[0][4]

    return feat, skill, level, description, source


def get_races():
    create_connection(DB_FILE)
    curr = CONN.cursor()

    query = 'SELECT  id, race, description FROM races'

    curr.execute(query)
    rows = curr.fetchall()

    raceID = rows[0][0]
    raceTitle = rows[0][1]
    raceDescription = rows[0][2]

    return raceID, raceTitle, raceDescription