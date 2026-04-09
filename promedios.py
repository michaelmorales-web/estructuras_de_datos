# Programa para recolectar datos
nombres = ["Leidy", "Dyaneris", "Esteban", "Rolando", "Diego"]
edades = [17, 15, 14, 15, 16]
musica = ["rock", "vallenato", "pop", "vocaloy", "cumbia"]
promedio_edades = sum(edades) / len(edades)
print("Promedio de edades:", promedio_edades)
mayores_15 = [edad for edad in edades if edad > 15]
print("Edades mayores de 15:", mayores_15)
rock = [m for m in musica if m == "rock"]
cantidad_rock = len(rock)
print("Personas que prefieren rock:", cantidad_rock)