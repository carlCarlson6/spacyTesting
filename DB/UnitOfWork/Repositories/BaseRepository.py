import pyodbc

class BaseRepository:
    def __init__(self, credentials):
        self.Connection = self.Connect(credentials)
        
    def Connect(self, credentials):
        driver = '{ODBC Driver 17 for SQL Server}'

        self.Connection = pyodbc.connect(
            'DRIVER='+driver+
            ';SERVER='+credentials['server']+
            ';PORT='+str(1433)+
            ';DATABASE='+credentials['database']+
            ';UID='+credentials['user']+
            ';PWD='+credentials['password']
        )
        return self.Connection

    def Query(self, QueryString):
        cursor = self.Connection.cursor()
        cursor.execute(QueryString)        
        rows = cursor.fetchall()
        return rows

    def getQueryString(self, queryFileName):
        queryString = None
        pathToQuery = 'DB/Queries/'+queryFileName
        with open(pathToQuery, 'r') as queryFile:
            queryString = queryFile.read()
        return queryString