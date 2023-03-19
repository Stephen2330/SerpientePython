#region importaciones

import pygame as PG
#endregion
#region variables y asignaciones
y, paso, cabeza = segmentos = [15, 16, 17]
n, manzana = paso, 99
pantalla = PG.display.set_mode([225] * 2, PG.SCALED).fill
#endregion

#region funcionalidad
while segmentos.count(cabeza) % 2 * cabeza % n * (cabeza & 240):
    if e:= PG.event.get(768):
        paso = (e[0].key % 4 * 17 + 15) % 49 - n
    segmentos = segmentos[manzana != cabeza:] + [cabeza + paso]
    pantalla('black')
    if manzana == cabeza:
        manzana = segmentos[0]
    for a, b in enumerate([manzana] + segmentos):
        pantalla('green' if a else 'red', ((b - 1) % n * y, (b - n) // n * y, y, y))
    PG.display.flip()
    cabeza += paso
    PG.time.wait(100)
#endregion