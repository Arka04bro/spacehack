#include <iostream>
#include <vector>
#include <string>

class AirManagement {
public:
    void regulateOxygen() {
        std::cout << "Regulating oxygen levels in the air...\n";
    }

    void removeCO2() {
        std::cout << "Removing CO2 from the air...\n";
    }

    void filterAir() {
        std::cout << "Filtering air to remove particles...\n";
    }
};

class WaterManagement {
public:
    void recycleWater() {
        std::cout << "Recycling water for reuse...\n";
    }

    void purifyWater() {
        std::cout << "Purifying water...\n";
    }
};

class FoodManagement {
public:
    void manageFood() {
        std::cout << "Managing food supplies for the crew...\n";
    }

    void prepareMeals() {
        std::cout << "Preparing meals...\n";
    }
};

class WasteManagement {
public:
    void processWaste() {
        std::cout << "Processing waste materials...\n";
    }

    void manageRecycling() {
        std::cout << "Managing recycling processes...\n";
    }
};

class HealthMonitoring {
public:
    void monitorHealth() {
        std::cout << "Monitoring crew health status...\n";
    }

    void checkRadiationLevels() {
        std::cout << "Checking radiation levels in the station...\n";
    }
};

class RecreationManagement {
public:
    void provideEntertainment() {
        std::cout << "Providing entertainment and leisure for the crew...\n";
    }

    void offerExercise() {
        std::cout << "Offering physical exercise equipment...\n";
    }
};

class SpaceStation {
private:
    AirManagement air;
    WaterManagement water;
    FoodManagement food;
    WasteManagement waste;
    HealthMonitoring health;
    RecreationManagement recreation;

public:
    void startLifeSupport() {
        std::cout << "Starting Life Support Systems...\n";

        air.regulateOxygen();
        air.removeCO2();
        air.filterAir();

        water.recycleWater();
        water.purifyWater();

        food.manageFood();
        food.prepareMeals();

        waste.processWaste();
        waste.manageRecycling();

        health.monitorHealth();
        health.checkRadiationLevels();

        recreation.provideEntertainment();
        recreation.offerExercise();

        std::cout << "Life Support Systems are fully operational.\n";
    }
};

int main() {
    SpaceStation station;
    station.startLifeSupport();

    return 0;
}
#include <iostream>
#include <vector>
#include <string>

class AirManagement {
public:
    void regulateOxygen() {
        std::cout << "Regulating oxygen levels in the air...\n";
    }

    void removeCO2() {
        std::cout << "Removing CO2 from the air...\n";
    }

    void filterAir() {
        std::cout << "Filtering air to remove particles...\n";
    }
};

class WaterManagement {
public:
    void recycleWater() {
        std::cout << "Recycling water for reuse...\n";
    }

    void purifyWater() {
        std::cout << "Purifying water...\n";
    }
};

class FoodManagement {
public:
    void manageFood() {
        std::cout << "Managing food supplies for the crew...\n";
    }

    void prepareMeals() {
        std::cout << "Preparing meals...\n";
    }
};

class WasteManagement {
public:
    void processWaste() {
        std::cout << "Processing waste materials...\n";
    }

    void manageRecycling() {
        std::cout << "Managing recycling processes...\n";
    }
};

class HealthMonitoring {
public:
    void monitorHealth() {
        std::cout << "Monitoring crew health status...\n";
    }

    void checkRadiationLevels() {
        std::cout << "Checking radiation levels in the station...\n";
    }
};

class RecreationManagement {
public:
    void provideEntertainment() {
        std::cout << "Providing entertainment and leisure for the crew...\n";
    }

    void offerExercise() {
        std::cout << "Offering physical exercise equipment...\n";
    }
};

class SpaceStation {
private:
    AirManagement air;
    WaterManagement water;
    FoodManagement food;
    WasteManagement waste;
    HealthMonitoring health;
    RecreationManagement recreation;

public:
    void startLifeSupport() {
        std::cout << "Starting Life Support Systems...\n";

        air.regulateOxygen();
        air.removeCO2();
        air.filterAir();

        water.recycleWater();
        water.purifyWater();

        food.manageFood();
        food.prepareMeals();

        waste.processWaste();
        waste.manageRecycling();

        health.monitorHealth();
        health.checkRadiationLevels();

        recreation.provideEntertainment();
        recreation.offerExercise();

        std::cout << "Life Support Systems are fully operational.\n";
    }
};

int main() {
    SpaceStation station;
    station.startLifeSupport();

    return 0;
}
