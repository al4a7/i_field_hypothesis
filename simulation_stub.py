import numpy as np

class IFieldSimulator:
    def __init__(self, N=10, coupling=0.1, dt=0.01, steps=1000):
        self.N = N  # number of oscillators
        self.coupling = coupling  # coupling strength
        self.dt = dt  # time step
        self.steps = steps  # simulation steps
        # Initialize phases randomly
        self.phases = np.random.rand(N) * 2 * np.pi

    def step(self):
        """Perform one simulation step using Kuramoto-like coupling."""
        mean_field = np.mean(np.exp(1j * self.phases))
        self.phases += self.dt * np.imag(mean_field * np.exp(-1j * self.phases)) * self.coupling

    def run(self):
        """Run full simulation and return phase history."""
        history = np.zeros((self.steps, self.N))
        for t in range(self.steps):
            self.step()
            history[t] = self.phases
        return history

if __name__ == "__main__":
    sim = IFieldSimulator(N=20, coupling=0.05, dt=0.02, steps=500)
    history = sim.run()
    coherence = np.abs(np.mean(np.exp(1j * history[-1])))
    print(f"Final coherence: {coherence:.3f}")
