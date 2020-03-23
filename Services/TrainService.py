import spacy
from spacy.util import minibatch, compounding
import random
from NerModel import *


class TrainService:
    def __init__(self, BlankModel, Language, Iterations):
        self.BlankModel = BlankModel
        self.Language = Language
        self.Iterations = Iterations

    def ExecuteTraining(self, TrainData):
        model = self.getInitialModel()
        model, disablePipelines = self.definePipeline(model, TrainData)
        model = self.Train(model, TrainData, disablePipelines)
        
        self.saveModel(model)

        trainedModel = NerModel(Ner = model)
        return trainedModel

    def getInitialModel(self):
        if self.BlankModel:
            model = spacy.blank(self.Language)
        else:
            model = spacy.load(self.Language+'_core_news_sm')
        return model

    def definePipeline(self, model, TrainData):
        if "ner" not in model.pipe_names:
            ner = model.create_pipe("ner")
            model.add_pipe(ner, last=True)

        model = self.addLabels(model, TrainData)

        pipeExceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
        disablePipelines = [pipe for pipe in model.pipe_names if pipe not in pipeExceptions]

        return model, disablePipelines 

    def addLabels(self, model, TrainData):
        allLabels = [entity.label for entity in document for document in TrainData.Documents]
        labels = list(set(allLabels))
        for label in labels:
            model.model.get_pipe("ner").add_label(label)
        return model

    def Train(self, model, TrainData):
        data = TrainData.getTrainData()

        if self.BlankModel:
            model.begin_training()
        
        for iteration in range(self.Iterations):
            random.shuffle(data)
            losses = {}
            
            batches = minibatch(data) 
            for batch in batches:
                text, annotations = zip(*batch)
                model.update(text, annotations, drop=0.5, losses=losses)
            
            print("Losses", losses)

        return model

    def saveModel(self, model):
        modelName = "ner_model_"+self.Language+"niter"+self.Iterations
        directory = "NerModel\\TrainnedModels\\"+modelName
        model.to_disk(directory)
        print('model saved')
        pass