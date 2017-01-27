from nltk.corpus import wordnet as wn

class Dictionary:
    
    
    def __init__(self,word):        
        self.word = word
        self.ss = wn.synsets(self.word)
        self.names = []
        self.id = []
        self.meanings = []
        self.synonyms = []
        self.antonyms = []
        self.examples = []

        

    def getSynsAndAntys(self):
        if not self.ss:
            return None
        for each in self.ss:
            for x in each.lemmas():
                self.synonyms.append(x.name())
                if x.antonyms():
                    self.antonyms.append(x.antonyms()[0].name())
        return (set(self.synonyms),set(self.antonyms))    


    def display(self,x=0):
        if not self.ss:
            return None
        
        for i in self.ss:
            self.id.append(i.name())
            self.names.append(i.lemmas()[0].name())
            self.meanings.append(i.definition())
            self.examples.append(i.examples())
        priv = self.getSynsAndAntys()
        '''
        if(x != 0):        
            #got all the data, now formatting starts
            print("_"*35)
            print(self.word,'\n')
            length = len(self.names)
            for i in range(length):
                print(self.names[i]+' :\t'+self.meanings[i])            
                for j in self.examples[i]:
                    print('Example: '+j)
                print('\n')
            print('_'*35)
            print('Synonyms:')
            for i in priv[0]:
                print(i.replace('_',' '))
            print('_'*35)
            print('Anonyms')
            for i in priv[1]:
                print(i.replace('_',' '))
         '''   
        
        return (self.names,self.meanings,self.examples,priv)
            
