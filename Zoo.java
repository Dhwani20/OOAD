import java.util.*;

class Animal
{
    private Boolean is_awake_;

    protected String name_;

    public void setName(String name)
    {
        name_=name;
    }

    public String getName()
    {
        return name_;
    }
    public void is_awake()
    {
        is_awake_=true;
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is awake");
    }

    public void is_eating()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is eating");
    }
    public void is_asleep()
    {
        is_awake_=false;
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is sleeping");
    }

    public void makeRandomSounds(){};
    public void run(){};

}
class Canine extends Animal
{
    public void run()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is running fast");
    }
}
class Feline extends Animal
{
    public void run()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is running gracefully");
    }
}

class Pachyderm extends Animal
{
    public void run()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" is running frantically");
    }
}
class Rhino extends Pachyderm
{
    public Rhino(String name)
    {
        name_=name;
    }
    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says, Look at my pointy nose!");
    }
}
class Hippo extends Pachyderm
{
    //Caused a constructor Overload

    public Hippo(String name)
    {
        name_=name;
    }

    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says, I love to swim");
    }
}

class Elephant extends Pachyderm
{
    public Elephant(String name)
    {
        name_=name;
    }
    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says, Listen to me play smooth jazz on my trumpet!");
    }
}
class Lion extends Feline
{
    public Lion(String name)
    {
        name_=name;
    }
    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says, REMEMBER WHO YOU ARE");
    }
}
class Tiger extends Feline
{
    public Tiger(String name)
    {
        name_=name;
    }
    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says my name is spelled TIGGER");
    }
}

class Cat extends Feline
{
    public Cat(String name)
    {
        name_=name;
    }

    public void makeRandomSounds() //Randomize the sounds the cat can make
    {
        Random rand = new Random();
        int n = rand.nextInt(3);

        switch(n)
        {
            case 0:
                System.out.println(name_+" the "+this.getClass().getSimpleName()+" meows softly");
                break;
            case 1:
                System.out.println(name_+" the "+this.getClass().getSimpleName()+" barks angrily");
                break;
            case 2:
                System.out.println(name_+" the "+this.getClass().getSimpleName()+" roars loudly");
                break;
           }
    }
}
class Dog extends Canine
{
    public Dog(String name)
    {
        name_=name;
    }
    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says I AM SO FLUFFY!");
    }
}

class Wolf extends Canine
{
    public Wolf(String name)
    {
        name_=name;
    }

    public void makeRandomSounds()
    {
        System.out.println(name_+" the "+this.getClass().getSimpleName()+" says I HATE TWILIGHT! ");
    }
}

class Zookeeper
{

    public void is_awake(List<Animal> zoo)
    {
        //wake up animals
        System.out.println("Wake up the animals in the zoo");
        for(Animal temp : zoo)
        {
            temp.is_awake();
        }
    }


    public void Attendance(List<Animal> zoo)
    {
        //check on animals
        System.out.println("Check if all animals are awake and present by each making random noises");
        for(Animal temp : zoo)
        {
            temp.makeRandomSounds();
        }
    }


    public void feedZoo(List<Animal> zoo)
    {
        //feed animals
        System.out.println("Feed the zoo their food");
        for(Animal temp : zoo)
        {
            temp.is_eating();
        }
    }


    public void exercise(List<Animal> zoo)
    {
 //make animals excercise
        System.out.println("Make the animals work out together");
        for(Animal temp : zoo)
        {
            temp.run();
        }
    }
//put the animals to sleep
    public void CloseZoo(List<Animal> zoo)
    {
        System.out.println("Put the animals to bed for the night");
        for(Animal temp : zoo)
        {
            temp.is_asleep();
        }
    }
}

class TestZoo
{
   public static void main(String[] args){
    {

   //create and list all instances of the animals
        List<Animal> zoo = new ArrayList<Animal>();


        Animal lion1 = new Lion("Harry Potter");
        Animal lion2 = new Lion("Neville Longbottom");
        Animal elephant1 = new Elephant("Ron Weasley");
        Animal elephant2 = new Elephant("Albus Dumbledore");
        Animal rhino1 = new Rhino("Choe Chang");
        Animal rhino2 = new Rhino("Peter Pettigrew");
        Animal tiger1 = new Tiger("Tom Riddle");
        Animal tiger2 = new Tiger("Draco Malfoy");
        Animal hippo1 = new Hippo("Severus Snape");
        Animal hippo2 = new Hippo("Luna Lovegood");
        Animal cat1 = new Cat("Hermione Granger");
        Animal cat2 = new Cat("Minerva McGonagall");
        Animal wolf1 = new Wolf("Rubeus Hagrid");
        Animal wolf2 = new Wolf("Remus Lupin");
        Animal dog1 = new Dog("Bellatrix Lestrange");
        Animal dog2 = new Dog("Sirius Black");

  //add the animals from the list to the zoo
        zoo.add(lion1);
        zoo.add(lion2);
        zoo.add(elephant1);
        zoo.add(elephant2);
        zoo.add(rhino1);
        zoo.add(rhino2);
        zoo.add(tiger1);
        zoo.add(tiger2);
        zoo.add(hippo1);
        zoo.add(hippo2);
        zoo.add(cat1);
        zoo.add(cat2);
        zoo.add(wolf1);
        zoo.add(wolf2);
        zoo.add(dog1);
        zoo.add(dog2);

        //make a new zookeeper run the zoo
        Zookeeper Filch = new Zookeeper();


        Filch.is_awake(zoo);
        Filch.Attendance(zoo);
        Filch.feedZoo(zoo);
        Filch.exercise(zoo);
        Filch.CloseZoo(zoo);
    }
}
}
