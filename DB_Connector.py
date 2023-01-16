#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
class DB_Connector:
    #database field is optional
    def __init__(self, host, user, password, database=None):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def print(self, query):
        self.cursor.execute(query)
        for line in self.cursor.fetchall():
            print(line)

    def commit(self):
        self.db.commit()

    def execute_and_commit(self, query, values=None):
        if values:
            self.cursor.executemany(query, values)
        else:
            self.cursor.execute(query)
        self.db.commit()

    def fetchall(self):
        return self.cursor.fetchall()
   
    def close(self):
        self.db.close()

def main():
    db = DB_Connector("10.10.10.40","killian","password")
    db.execute("use hotels;")


    #Recuperation de la liste des nom d'hotels
    liste_nomhot=[]
    db.execute("SELECT DISTINCT nomhot from HOTEL_CHAMBRE;")
    for nomhot in db.fetchall():
        liste_nomhot.append(nomhot[0])

    #affichage de l'hotel selectionne
    hotel=input(f"Selectionner un hotel {liste_nomhot}: ")
    db.execute(f"SELECT nomhot from HOTEL_CHAMBRE WHERE nomhot='{hotel}';")
    db.close()