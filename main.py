import DB
from DB import DocumentsRepository
from Models import TrainData


documentsRepository = DocumentsRepository(DB.DatabaseCredentials)
trainData = TrainData(Documents=documentsRepository.GetDocuments())




K = 0