
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

class Dashboard {
    public void display() {
        System.out.println("Dashboard lights up");
    }
}

class GPS {
    public void gpsActivated() {
        System.out.println("GPC Activated");
    }
}

class Vehicle {
    private Engine engine;
    private Dashboard dashboard; // composition
    private GPS gps; // aggregation

    public Vehicle(Engine engine) {
        this.engine = engine; // Dependency injection
        dashboard = new Dashboard();
        // this.gps = gps;
    }

    public void AddGps(GPS gps) {
        this.gps = gps;
    }

    public void start() {
        engine.start();
        if (gps != null) {
            gps.gpsActivated();
        }

        dashboard.display();

    }

}

public class Aggregation {
    public static void main(String[] args) {
        GasolineEngine gas = new GasolineEngine();
        GPS gps = new GPS();
        Vehicle mycar = new Vehicle(gas); // Dependency injection
        mycar.AddGps(gps);
        mycar.start();
    }
}
