class DictSubclass(dict):
    def __repr__(self):
        return "DictSubclass"

dict.fromkeys("abc")        
