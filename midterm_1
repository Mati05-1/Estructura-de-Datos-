import time
import queue
import memory_profiler
import pandas as pd
import cProfile
import pstats
import io
import matplotlib.pyplot as plt
from line_profiler import LineProfiler

class CustomQueue:
    def __init__(self):
        self.q = queue.Queue()
    
    def insert_elements(self, n):
        """Inserta n elementos, asegurando que tome al menos 1 segundo."""
        start_time = time.time()
        for i in range(n):
            self.q.put(i)
            time.sleep(max(1/n, 0.01))  
        end_time = time.time()
        return end_time - start_time
    
    def profile_and_save(self, pr, filename):
        """Guarda el resultado del perfilador en un archivo de texto."""
        with open(filename, "w") as f:
            ps = pstats.Stats(pr, stream=f).sort_stats(pstats.SortKey.TIME)
            ps.print_stats()
    
    def line_profile_and_save(self, lp, filename):
        """Guarda el resultado de line_profiler en un archivo de texto."""
        with open(filename, "w") as f:
            lp.print_stats(stream=f)

    @memory_profiler.profile
    def linear_search(self, target, filename):
        """Búsqueda lineal manual en la cola, guardando el perfil en un archivo."""
        pr = cProfile.Profile()
        pr.enable()
        
        lp = LineProfiler()
        lp_wrapper = lp(self._linear_search_impl)
        found = lp_wrapper(target)
        
        pr.disable()
        self.profile_and_save(pr, filename)
        self.line_profile_and_save(lp, filename.replace(".txt", "_line.txt"))
        return found

    def _linear_search_impl(self, target):
        """Implementación interna de búsqueda lineal para line_profiler."""
        temp_list = list(self.q.queue)
        for item in temp_list:
            time.sleep(0.0001)  
            if item == target:
                return True
        return False
    
    @memory_profiler.profile
    def delete_element(self, filename):
        """Elimina un elemento de la cola (dequeue) y guarda el perfil en un archivo."""
        pr = cProfile.Profile()
        pr.enable()
        
        result = None
        if not self.q.empty():
            result = self.q.get()
        
        pr.disable()
        self.profile_and_save(pr, filename)
        return result


sizes = [1000, 2000, 3000, 4000, 5000]  
search_times = []
delete_times = []

for size in sizes:
    q = CustomQueue()
    q.insert_elements(size)

    
    start_time = time.time()
    q.linear_search(-1, f"profile_search_{size}.txt")  
    search_times.append(time.time() - start_time)

   
    start_time = time.time()
    q.delete_element(f"profile_delete_{size}.txt")
    delete_times.append(time.time() - start_time)


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
