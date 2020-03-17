class TrainData:
    def __init__(self, Documents=None):
        self.Documents=None

    def GetTrainData(self):
        trainData = []

        for document in self.Documents:
            trainEntities = [(entity.InitPosition, entity.EndPosition, entity.Label) for entity in document.Entities]
            trainData.append((document.Text), {'entities': trainEntities})

        return trainData