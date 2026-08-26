#CONTROLER TEMPERATURE
class ControlerTemperature:
    def __init__(self, temperature, unit):
        self._temperature = temperature
        self._unit = unit

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 16 or value > 30:
            raise ValueError("Temperature must be between 16 and 30")
        self._temperature = value
        
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if value not in ["C", "F"]:
            raise ValueError("Unit must be 'C' or 'F'")
        self._unit = value

t1 = ControlerTemperature(25, "F")
print(t1.temperature)