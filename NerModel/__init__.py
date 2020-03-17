import spacy
from Models import Entity

class NerModel:
    def __init__(self, Ner):
        self.Ner = Ner

    def RecognizeEntities(self, Text):
        processedText = self.Ner(Text)

        entities = []
        for entity in processedText.ents:
            entities.append(Entity(Text=entity.text, Label=entity.label_))

        return entities

    @staticmethod
    def Load(path):
        ner = spacy.load(path)
        return NerModel(ner) 