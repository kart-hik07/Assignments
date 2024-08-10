import numpy as np

g = 9.81
rho_water = 1000
rho_air = 1.225
Cd = 0.8
A = 0.01
V_bottle = 0.00225
m_bottle = 0.15


def water_rocket_simulation(V_water0, launch_angle, wind_speed, wind_angle, dt=0.01, t_max=10):
    angle_rad = np.radians(launch_angle)
    wind_angle_rad = np.radians(wind_angle)
    
    wind_vx = wind_speed * np.cos(wind_angle_rad)
    wind_vy = wind_speed * np.sin(wind_angle_rad)

    vx = wind_vx
    vy = wind_vy
    t = 0
    y = 0
    x = 0
    V_water = V_water0
    m_water = V_water * rho_water
    m_total = m_bottle + m_water
    V_air = V_bottle - V_water
    m_air = (P0 * V_air) / (rho_air * g)

    while t < t_max:
        if V_water > 0:
            thrust = (P0 * (V_bottle - V_water)) / (rho_air * g) * (V_water / V_bottle)
        else:
            thrust = 0

        drag = 0.5 * Cd * A * rho_air * (vx**2 + vy**2)
        ax = (thrust - drag) * np.cos(angle_rad) / m_total
        ay = (thrust - drag) * np.sin(angle_rad) / m_total - g

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        if y < 0:
            break

        V_water -= dt * 0.01
        m_water = max(0, V_water * rho_water)
        m_total = m_bottle + m_water
        V_air = V_bottle - V_water
        m_air = (P0 * V_air) / (rho_air * g)

        t += dt

    return x

V_water0 = float(input("vol of water(litres): ")) / 1000
launch_angle = float(input("launch angle: "))
wind_speed = float(input("wind speed: "))
wind_angle = float(input("wind direction angle: "))

distance = water_rocket_simulation(V_water0, launch_angle, wind_speed, wind_angle)

print(f"Distance traveled: {distance:.2f} m")
