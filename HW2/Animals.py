
#!/usr/bin/python3
from random import choice , random
from TheObservedZoo import Message

# === ZOOtils ==========================================================================================================

def flip_weighted( truProb ):
    """ Return True with probability 'truProb' , Otherwise return False """
    return random() <= truProb

# ___ End Helpers ______________________________________________________________________________________________________


# === The STRATEGY Pattern =============================================================================================

class STRAT_moveFly:
    """ The FLY strategy, for those without patience """
    
    def __init__( self , animal ):
        """ Assign the `Animal` that deploys this strategy """
        self.ani = animal
        
    def __call__( self ):
        """ State name, choose mood, and announce the movement strategy used """
        print( '\t' , self.ani.name , choice( self.ani.moodAdv ) , "**flies** about." )


class STRAT_moveStalk:
    """ The STALK strategy, for the quiet ones """
    
    def __init__( self , animal ):
        """ Assign the `Animal` that deploys this strategy """
        self.ani = animal
        
    def __call__( self ):
        """ State name, choose mood, and announce the movement strategy used """
        print( '\t' , self.ani.name , choice( self.ani.moodAdv ) , "**stalks** about." )


class STRAT_moveAmble:
    """ The AMBLE strategy, for those with patience """
    
    def __init__( self , animal ):
        """ Assign the `Animal` that deploys this strategy """
        self.ani = animal
        
    def __call__( self ):
        """ State name, choose mood, and announce the movement strategy used """
        print( '\t' , self.ani.name , choice( self.ani.moodAdv ) , "**ambles** about." )

# ___ End STRATEGY _____________________________________________________________________________________________________

class Animal:
    """ A noisy, hungry eukaryote """
    
    moodAdv = [
        "ECSTATICALLY" ,
        "HAPPILY" ,
        "AMBIVALENTLY" ,
        "GLUMLY" ,
        "DEJECTEDLY" ,
    ]

    def __init__( self , zoo , name , sigNoise ):
        """ Init the necessary data to perform activities of the day """
        self.zoo   = zoo # ---- Animal notifies this zoo, if necessary
        self.name  = name # --- How this Animal is identified
        self.saySo = sigNoise # Signature noise for this animal
        
    def get_name( self ):
        """ We need to know whom does what """
        return self.name
        
    def wakeup( self ):
        """ Response to being woken up """
        print( '\t' , self.name , "wakes up..." )
        
    def make_noise( self ):
        """ Response to roll call """
        print( '\t' , self.name , "says" , self.saySo )
        
    def roam( self ):
        """ Response to exercise , REPLACE WITH STRATEGY """
        raise NotImplementedError( "A STRAT belongs here!" )
        
    def eat( self ):
        """ Response to being fed """
        print( "\tThis is the best food" , self.name , "will ever taste." )
        self.flourish()
        
    def sleep( self ):
        """ Response to bedtime story """
        print( "\t" , self.name , "has had just about enough. Time to sleep." )
        
    def flourish( self ):
        """ An extra random behavior """
        # NOTE: This function overridden at various levels of inheritance
        if flip_weighted( 0.25 ):
            print( "\t" , self.name , "isn't particularly interesting." )
            self.zoo.receive( Message( 'ani' , None ) )
            
            
class Bird( Animal ):
    """ A winged dinosaur """
    
    def __init__( self , zoo , name ,  sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )
        self.roam = STRAT_moveFly( self ) # STRATEGY Pattern
        
    def flourish( self ):
        """ An extra random behavior """
        if flip_weighted( 0.25 ):
            print( "\t" , self.name , "flaps wildly in circles." )
            self.zoo.receive( Message( 'ani' , None ) ) 
        
        
class Feline( Animal ):
    """ A pointier, meaner dog """
    def __init__( self , zoo , name , sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )
        self.roam = STRAT_moveStalk( self ) # STRATEGY Pattern
        
class Pachyderm( Animal ):
    """ A giant muscle fortress """
    def __init__( self , zoo , name , sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )
        self.roam = STRAT_moveAmble( self ) # STRATEGY Pattern
        
class Macaw( Bird ):
    """ The noisiest dinosaur """
    def __init__( self , zoo , name , sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )


class Tiger( Feline ):
    """ The pointiest, meanest dog (DO NOT PET) """
    
    def __init__( self , zoo , name , sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )
        
    def flourish( self ):
        """ An extra random behavior """
        if flip_weighted( 0.25 ):
            print( "\t" , self.name , "eyes the Zookeeper hungrily." )
            self.zoo.receive( Message( 'ani' , None ) )


class Elephant( Pachyderm ):
    """ A living castle with an arm on its face, because why not? """

    def __init__( self , zoo , name , sigNoise ):
        """ Assign necessary parameters for being an Animal """
        super().__init__( zoo , name , sigNoise )
        
    def flourish( self ):
        """ An extra random behavior """
        if flip_weighted( 0.25 ):
            print( "\t" , self.name , "knocks over a tree." )
            self.zoo.receive( Message( 'ani' , None ) )
