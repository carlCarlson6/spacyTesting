from DB.UnitOfWork.Repositories.BaseRepository import BaseRepository
from Models import Entity
import re


class EntitiesRepository(BaseRepository):
    def __init__(self, credentials):
        super().__init__(credentials)
        self.QueryString = self.getQueryString('EntitiesQuery.sql')

    def GetEntitiesInDocument(self, DocId):
        entities = []
        queryString = self.QueryString.replace('<DocumentId>', DocId)
        rows = self.Query(queryString)
        
        for row in rows:
            entity = Entity(Id=row[0], InitPosition=row[1], EndPosition=row[1]+row[2], Label=row[3])
            entities.append(entity)

        return entities