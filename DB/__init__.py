import json
import pyodbc

from DB.UnitOfWork.Repositories.DocumentsRepository import DocumentsRepository

DatabaseCredentials = {}
with open('local.settings.json', 'r') as jsonFile:
    DatabaseCredentials = json.load(jsonFile)["SQL"]