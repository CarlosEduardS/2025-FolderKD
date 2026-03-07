class Neuron:
    def __init__(self,pergunta: str):
        self.per = pergunta
    
    def interrogativa(self):
        self.inte = ['qual','ql','quem','qm','que','q','quais','qls','quantos','qnts','qntas','quantas','quanto','qnt','quanta','qnta','onde','ond','quando','qnd']
        match self.inte:
            case _ if self.inte[:1]:
                self.note = {'interrogativa':self.inte[0:1]}
            case _ if self.inte[2:3]:
                self.note = {'interrogativa':self.inte[2:3]}
            case _ if self.inte[4:5]:
                self.note = {'interrogativa':self.inte[4:5]}
            case _ if self.inte[6:7]:
                self.note = {'interrogativa':self.inte[6:7]}
            case _ if self.inte[8:9]:
                self.note = {'interrogativa':self.inte[8:9]}
            case _ if self.inte[10:11]:
                self.note = {'interrogativa':self.inte[10:11]}
            case _ if self.inte[12:13]:
                self.note = {'interrogativa':self.inte[12:13]}
            case _ if self.inte[14:15]:
                self.note = {'interrogativa':self.inte[14:15]}
            case _ if self.inte[16:17]:
                self.note = {'interrogativa':self.inte[16:17]}
            case _ if self.inte[18:19]:
                self.note = {'interrogativa':self.inte[18:19]}
    
    def conclusao(self):
        self.con = ['portanto', 'logo', 'assim', 'em conclusão', 'em síntese', 'enfim', 'por conseguinte', 'por isso', 'concluindo', 'consequentemente']
    
    def oposiçao(self):
        pass
    
    def suposiçao(self):
        pass