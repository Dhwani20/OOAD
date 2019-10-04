
class User:
    def __init__( self ):
        self.strat = None
        self.name  = "USER"

class Tool:
    def __init__( self , usr ):
        self.user = usr
    def __call__( self ):
        print( self.user.name , "used a TOOL" )

foo       = User()
foo.strat = Tool( foo )

foo.strat()
