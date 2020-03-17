class Document:
    def __init__(self, Id:str, Text:str, Entities=None):
        self.Id = Id
        self.Text = Text
        self.Entities = Entities