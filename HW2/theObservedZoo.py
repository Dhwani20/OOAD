# TheObservedZoo.py
# James Watson, Dhwani Khatter
# FIXME: DO NOT ADD ANY FUNCTIONALITY BEYOND THE SPEC!

from collections import namedtuple , deque

from Animals import *

# === The OBSERVER Pattern =============================================================================================

Message = namedtuple( 'Message' , [ 'type' , 'msg' ] ) # Communication between objects with Loose Coupling

class Zoo:
    """ A place where animals live, things happen, and people *want to KNOW about it* ! """

    def __init__( self ):
        """ Create structures to distribute messages """
        # ~ Observer Vars ~
        self.MSG_subscribers = {} # ---- Lookup for who gets messages of each type , Type maps to list of subscribers
        self.MSG_Queue       = deque() # Message queue, flush and process when convenient
        self.animals         = [] # ---- Container for all of the animals

    # == A message broker for the Observer Pattern ==
    # Note in this implementation there is no publisher list and anyone can dump messages in

    def receive( self , msg ):
        """ Add the `msg` to the queue """
        self.MSG_Queue.append( msg ) # Add a message to the back of the queue
        self.process_queue() # NOTE: In order for the announcer's messages to be processed before the effects of the
        #                            Zookeeper's actions are printed, each message is handled **immediately**

    def add_subscriber( self , sub , msgType ):
        """ Add a listener for a specific message type """
        if msgType in self.MSG_subscribers: # If the message type exists in the lookup, append
            self.MSG_subscribers[ msgType ].append( sub )
        else: # Else add a new message type to the registry
            self.MSG_subscribers[ msgType ] = [ sub ]

    def process_queue( self ):
        """ Deliver all messages in the queue """
        # 0. For each message in the queue
        while len( self.MSG_Queue ):
            # 1. Fetch message
            msg = self.MSG_Queue.popleft()
            # 2. Try to deliver the message to each of the subscribers of this type
            try:
                subs = self.MSG_subscribers[ msg.type ]
                for sub in subs:
                    # NOTE: Every subscriber MUST have a `receive` method! (Would have an interface for more complex app)
                    sub.receive( msg )
            except KeyError:
                print( "MessageBus.process_queue: Message type" , msg.type , "has no subscribers!\nDropped:" , msg.msg )

    # __ End Broker __

# ___ End OBSERVER ____________________________________________________________________________________________________

class Zookeeper:
    """ Zookeper is a Human """

    def __init__( self , zoo , name ):
        """ Assign workplace and name """
        self.zoo  = zoo # Broker that all of the keeper messages go to
        self.name = name
        self.zoo.add_subscriber( self , 'ani' ) # Subscribe to animal events, and make comments about them

    def receive( self , msg ):
        """ Response to `ani` messages """
        print( "Zookeeper: Now *that* was odd!" )

    def wake( self , ani ):
        """ Awaken target and send a message """
        self.zoo.receive( Message( 'keeper' , { 'wake' : ani.get_name() } ) )
        print( self.name , "WAKES" , ani.get_name() )
        ani.wakeup();

    def roll_call( self , ani ):
        """ Prompt target, trigger noise and send a message """
        self.zoo.receive( Message( 'keeper' , { 'call' : ani.get_name() } ) )
        print( self.name , "CALLS" , ani.get_name() )
        ani.make_noise()

    def feed( self , ani ):
        """ Feed target , trigger message and send a message """
        self.zoo.receive( Message( 'keeper' , { 'feed' : ani.get_name() } ) )
        print( self.name , "FEEDS" , ani.get_name() )
        ani.eat()

    def exercise( self , ani ):
        """ Exercise target and send a message """
        self.zoo.receive( Message( 'keeper' , { 'walk' : ani.get_name() } ) )
        print( self.name , "WALKS" , ani.get_name() )
        ani.roam()

    def shut_down( self ,  ani ):
        """ Put target to bed , Trigger message and send a message """
        self.zoo.receive( Message( 'keeper' , { 'read' : ani.get_name() } ) )
        print( self.name , "READS A STORY TO" , ani.get_name() )
        ani.sleep()


class ZooAnnouncer:
    """ Likes to talk """

    def __init__( self , zoo ):
        """ Connect to the Zoo as a subscriber and set flags for the beginning of each activity """
        self.zoo = zoo # Listens here for the `Zookeeper` activities
        self.zoo.add_subscriber( self , 'keeper' )
        self.woke   = 0 # Has the awakening begun?
        self.called = 0 # Has the roll call begun?
        self.fed    = 0 # Has the foodening begun?
        self.walked = 0 # Has exercise started?
        self.closed = 0 # Has shutdown begun?

    def receive( self , msg ):
        """ Respond to 'keeper' messages , Will announce an activity type for the first message of that type, not after """
        if ( 'wake' in msg.msg ) and ( not self.woke ):
            print( "\n~~~" , "ZooAnnouncer: The Zookeeper is about to wake the animals!" , "~~~\n" )
            self.woke = 1
        if ( 'call' in msg.msg ) and ( not self.called ):
            print( "\n~~~" , "ZooAnnouncer: Roll call!" , "~~~\n" )
            self.called = 1
        if ( 'feed' in msg.msg ) and ( not self.fed ):
            print( "\n~~~" , "ZooAnnouncer: The Zookeeper is about to feed the animals!" , "~~~\n" )
            self.fed = 1
        if ( 'walk' in msg.msg ) and ( not self.walked ):
            print( "\n~~~" , "ZooAnnouncer: The Zookeeper is about to exercise the animals!" , "~~~\n" )
            self.walked = 1
        if ( 'read' in msg.msg ) and ( not self.closed ):
            print( "\n~~~" , "ZooAnnouncer: The Zookeeper is closing the Zoo!  Please make your way to the exit." , "~~~\n" )
            self.closed = 1

if __name__ == '__main__':

    # 1. Create Zoo and add Animals
    theZoo = Zoo()

    # 2. Create and attach Zookeeper
    zKeeper = Zookeeper( theZoo , "Zookeeper" )

    # 3. Create and attach ZooAnnouncer
    announcer = ZooAnnouncer( theZoo )

    # 4. Populate the Zoo
    theZoo.animals.append( Macaw( theZoo , "Margaret Macaw" , "Caw Caw!" ) )
    theZoo.animals.append( Macaw( theZoo , "Michael Macaw" , "Caw Caw!" ) )
    theZoo.animals.append( Tiger( theZoo , "Tina Tiger" , "ROAR!" ) )
    theZoo.animals.append( Tiger( theZoo , "Thomas Tiger" , "ROAR!" ) )
    theZoo.animals.append( Elephant( theZoo , "Ellie Elephant" , "FFhhhnoouuugh!" ) )
    theZoo.animals.append( Elephant( theZoo , "Edward Elephant" , "FFhhhnoouuugh!" ) )

    # 5. Simulate one day at the zoo
    # A. Wake
    for ani in theZoo.animals:
        zKeeper.wake( ani )
    # B. Call
    for ani in theZoo.animals:
        zKeeper.roll_call( ani )
    # C. Feed
    for ani in theZoo.animals:
        zKeeper.feed( ani )
    # D. Walk
    for ani in theZoo.animals:
        zKeeper.exercise( ani )
    # E. Close
    for ani in theZoo.animals:
        zKeeper.shut_down( ani )

    
