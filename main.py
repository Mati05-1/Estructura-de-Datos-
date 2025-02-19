import time
import queue
import memory_profiler
import pandas as pd
import cProfile
import pstats
import io
import matplotlib.pyplot as plt

class CustomQueue:
    def __init__(self):
        self.q = queue.Queue()
    
    def insert_elements(self, n):
        """Inserta n elementos, asegurando que tome al menos 1 segundo."""
        start_time = time.time()
        for i in range(n):
            self.q.put(i)
            time.sleep(max(1/n, 0.01))  # Control del tiempo mínimo
        end_time = time.time()
        return end_time - start_time
    
    @memory_profiler.profile
    def linear_search(self, target):
        """Búsqueda lineal manual en la cola."""
        pr = cProfile.Profile()
        pr.enable()
        
        temp_list = list(self.q.queue)  # Convertimos la cola en una lista temporal
        for item in temp_list:
            if item == target:
                pr.disable()
                s = io.StringIO()
                ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
                ps.print_stats()
                print(s.getvalue())  # Muestra el perfil en la terminal
                return True
        
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
        ps.print_stats()
        print(s.getvalue())  # Muestra el perfil en la terminal
        return False
    
    @memory_profiler.profile
    def delete_element(self):
        """Elimina un elemento de la cola (dequeue)."""
        pr = cProfile.Profile()
        pr.enable()
        
        result = None
        if not self.q.empty():
            result = self.q.get()
        
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
        ps.print_stats()
        print(s.getvalue())  # Muestra el perfil en la terminal
        return result

# Prueba con diferentes tamaños
sizes = [10, 20, 30, 40, 50]  # Tamaños de las colas
search_times = []
delete_times = []

for size in sizes:
    q = CustomQueue()
    q.insert_elements(size)

    # Medir tiempo de búsqueda
    start_time = time.time()
    q.linear_search(-1)  # Buscando un número que NO está
    search_times.append(time.time() - start_time)

    # Medir tiempo de eliminación
    start_time = time.time()
    q.delete_element()
    delete_times.append(time.time() - start_time)

# Guardar en DataFrame
df = pd.DataFrame({'Tamaño': sizes, 'Tiempo_Search': search_times, 'Tiempo_Delete': delete_times})
print(df)

# Graficar
plt.plot(sizes, search_times, label="Search Time", marker="o")
plt.plot(sizes, delete_times, label="Delete Time", marker="s")
plt.xlabel("Tamaño de la Cola")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución de Search y Delete en Queue")
plt.legend()
plt.grid(True)
plt.savefig("performance.png")
plt.show()
