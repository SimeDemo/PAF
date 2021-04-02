import particle as prt
from math import cos, sin, sqrt

p1 = prt.Particle(10, 45, 5, 5)

p1.range_p(0.001)
p1.plot_trajectory()

analy = p1.analytically() 
numerically = p1.range_p(0.001)

error = abs(analy - numerically) / analy 

print(f"odstupanje je {error * 100}%")

p1.total_time(0.001)

p1.max_speed()

p1.velocity_to_hit_target()