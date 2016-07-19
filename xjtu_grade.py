class XjtuGrade:

    def __init__(self):
        self.term       =   None
        self.code       =   None
        self.name       =   None
        self.type       =   None
        self.status     =   None
        self.credit     =   None
        self.reason     =   None
        self.nature     =   None
        self.vaild      =   None
        self.grades     =   {
            'main'      : 100,
            'standard'  : 100,
            'daily'     : 100,
            'interim'   : 100,
            'expr'      : 100,
            'final'     : 100,
            'other'     : 100
        }

    def __str__(self):
        return '%s\n%s\n%s\n%s\n%s\n%s\t%s\t%s\t%s\t%s\t%s\t%s\n%s\n%s\n%s\n%s' % (self.term, self.code, self.name, self.type, self.status,
            self.grades['main'], self.grades['standard'], self.grades['daily'],
            self.grades['interim'], self.grades['expr'], self.grades['final'],
            self.grades['other'], self.credit, self.reason, self.nature, self.vaild)



        


