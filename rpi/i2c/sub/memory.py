# Bibliotheken laden
import gc
import os

# Funktion: Arbeitsspeicher
def access_memory():
    gc.collect()
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F + A
    P = (F / T) * 100
    print('Arbeitsspeicher Gesamt: {0:.2f} MB / Frei: {1:.2f} MB ({2:.1f} %)'.format(T/1000, F/1000, P))
    return P

# Funktion: Flash-Memory
def flash_memory():
    mebibyte = 1024 * 1024
    s = os.statvfs('//')
    T = (s[0] * s[2]) / mebibyte
    F = (s[0] * s[3]) / mebibyte
    P = (F / T) * 100
    print('Flash-Memory Gesamt: {0:.4f} MiB / Frei: {1:.4f} MiB ({2:.1f} %)'.format(T, F, P))
    return P
