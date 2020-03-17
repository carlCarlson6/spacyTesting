import spacy
from spacy.util import minibatch, compounding


class TrainService:
    def __init__(self, BlankModel, Language):
        self.BlankModel = BlankModel
        self.Language = Language

    def ExecuteTrain(self, TrainData):
        model = self.getInitialModel()
        model = self.definePipeline(model)
        
        pass

    def getInitialModel(self):
        if self.BlankModel:
            model = spacy.blank(self.Language)
        else:
            model = spacy.load(self.Language+'_core_news_sm')
        return model

    def definePipeline(self, InitialModel):
        pass

    def addLabels(self, model, TrainData):
        allLabels = [entity.label for entity in document for document in TrainData.Documents]
        labels = list(set(allLabels))
        for label in labels:
            model.add_label(label)
        return model

    def train(self, model):
        pass

    def saveModel(self, model):
        pass