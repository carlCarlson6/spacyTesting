from DB.UnitOfWork.Repositories.BaseRepository import BaseRepository
from DB.UnitOfWork.Repositories.EntitiesRepository import EntitiesRepository
from Models import Document


class DocumentsRepository(BaseRepository):
    def __init__(self, credentials):
        super().__init__(credentials)
        self.QueryString = self.getQueryString('DocumentsQuery.sql')
        self.entitiesRepository = EntitiesRepository(credentials)

    def GetDocuments(self):
        documents = []
        rows = self.Query(self.QueryString)

        for row in rows:
            doc = Document(Id=row[0], Text=row[1])
            doc.Entities = self.entitiesRepository.GetEntitiesInDocument(doc.Id)
            documents.append(doc)

        return documents
            

            
        