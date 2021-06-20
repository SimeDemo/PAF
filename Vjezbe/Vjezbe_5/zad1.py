import harmonic_oscillator as ho 

h1 = ho.HarmonicOscillator(10, 5, 5, 5, 50)

h1.oscillate(0.01)
h1.oscillate(0.001)

h1.plot_oscillation()
