
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

class Dashboard{
    public void display(){
        System.out.println("Dashboard lights up");
    }
}

class Vehicle {
    private Engine engine;
    private Dashboard dashboard; // composition

    public Vehicle(Engine engine) {
        this.engine = engine; // Dependency injection
        dashboard = new Dashboard();
    }

    public void start() {
        engine.start();
        dashboard.display();

    }
}

public class Composition {
    public static void main(String[] args) {
        // GasolineEngine gas = new GasolineEngine();
        // Vehicle veh = new Vehicle(gas); // Dependency injection
    }
}
