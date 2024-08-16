
interface Engine {
    public void start();
} 

class GasolineEngine implements Engine {
    public void start() {
        System.out.println("Gasoline engine starts with ignition.");
    }
}

class ElectricEngine implements Engine {
    public void start() {
        System.out.println("Electric engine starts silently.");
    }
}

class Vehicle{
    private Engine engine;

    public Vehicle(Engine engine){
        this.engine = engine;   // Dependency injection
    }
    public void start(){
        engine.start();
    }
}

public class Losse_coupling {
    public static void main(String[] args) {
    // GasolineEngine gas = new GasolineEngine();
    // Vehicle veh = new Vehicle(gas);  // Dependency injection
    }
}
