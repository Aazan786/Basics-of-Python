class GasolineEngine{
    // private String engine_name;

    public void start(){
        System.out.println("Gasoline engine starts with ignition.");
    }
}

class Vehicle{
    private GasolineEngine engine;

    public Vehicle(){
        engine = new GasolineEngine(); // Vehicle directly depends on GasolineEngine
    }

    public void start(){
        engine.start();
    }
}

public class Tight_coupling {
    public static void main(String[] args) {
        
    }
}
