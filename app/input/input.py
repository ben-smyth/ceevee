class BaseInput():
    def __init__(
        self, 
        input_path: str
    ):
        self.input_path = input_path
    
    def convertToString(self):
        raise NotImplementedError("convertToString() not implemented")
