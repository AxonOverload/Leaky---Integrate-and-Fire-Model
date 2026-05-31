class LIF:
    
    def __init__(self, V_rest, resistance, input_current, tau, V_threshold, V_reset):
        self.V_rest = V_rest
        self.resistance = resistance
        self.input_current = input_current
        self.tau = tau
        self.V_threshold = V_threshold
        self.V_reset = V_reset
        self.V = V_rest
        
    def step(self, dt):
        
        self.V += (-(self.V - self.V_rest) + self.resistance * self.input_current) / self.tau * dt
        
        
        if self.V >= self.V_threshold:
            spiking_times.append(i)
            print(f"Spike at time step {i}, Voltage: {self.V:.2f} mV")
            self.V = self.V_reset 




neuron = LIF(V_rest=-70, resistance=10, input_current=2, tau=20, V_threshold=-55, V_reset=-70)

voltages = []
spiking_times = []

for i in range(100):
    neuron.step(dt=1)
    
    
    voltages.append(neuron.V)
    
   
   
import matplotlib.pyplot as plt


plt.plot(voltages)
plt.xlabel("TimeStep")
plt.ylabel("Membrane Voltage (mV)")
plt.axhline(y=-55, color='red', linestyle='--', label='Threshold')
plt.title("LIF Neuron")
plt.legend()
plt.show()
