import random

# Algoritmo First Come First Serve (FCFS)
def fcfs(processes):
    # Ordenamos los procesos por tiempo de llegada (arrival_time)
    processes.sort(key=lambda x: x['arrival_time'])
    current_time = 0  # Tiempo actual de la CPU
    waiting_time = 0  # Tiempo total de espera de todos los procesos

    # Recorrer todos los procesos y calcular el tiempo de espera
    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']  # Si la CPU está libre, espera hasta que llegue el siguiente proceso
        waiting_time += current_time - process['arrival_time']  # Tiempo que el proceso espera antes de ejecutarse
        current_time += process['burst_time']  # Actualizamos el tiempo actual después de ejecutar el proceso

    avg_waiting_time = waiting_time / len(processes)  # Calculamos el tiempo de espera promedio
    return avg_waiting_time
    
# Algoritmo Shortest Job First (SJF)
def sjf(processes):
     # Ordenamos los procesos por tiempo de llegada y, en caso de empate, por tiempo de ejecución (burst_time)
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))
    current_time = 0  # Tiempo actual de la CPU
    waiting_time = 0  # Tiempo total de espera de todos los procesos

    # Recorrer todos los procesos y calcular el tiempo de espera
    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']  # Si la CPU está libre, espera hasta que llegue el siguiente proceso
        waiting_time += current_time - process['arrival_time']  # Tiempo que el proceso espera antes de ejecutarse
        current_time += process['burst_time']  # Actualizamos el tiempo actual después de ejecutar el proceso

    avg_waiting_time = waiting_time / len(processes)  # Calculamos el tiempo de espera promedio
    return avg_waiting_time


# Algoritmo Round Robin (RR)
def round_robin(processes, quantum):
    queue = processes.copy()  # Copiamos los procesos a una cola de espera
    current_time = 0  # Tiempo actual de la CPU
    waiting_time = {process['pid']: 0 for process in processes}  # Diccionario para rastrear el tiempo de espera de cada proceso
    remaining_time = {process['pid']: process['burst_time'] for process in processes}  # Tiempo de ejecución restante por proceso

    # Procesamos los procesos en la cola utilizando el quantum
    while queue:
        process = queue.pop(0)  # Extraemos el primer proceso de la cola

        if current_time < process['arrival_time']:
            current_time = process['arrival_time']  # Si la CPU está libre, espera hasta que llegue el siguiente proceso

        # Si el tiempo restante del proceso es mayor que el quantum, ejecutamos por el quantum y volvemos a insertar
        if remaining_time[process['pid']] > quantum:
            remaining_time[process['pid']] -= quantum
            current_time += quantum  # Avanzamos el tiempo
            queue.append(process)  # Reinserta el proceso al final de la cola
        else:
            # El proceso finaliza en esta ronda
            current_time += remaining_time[process['pid']]  # Actualizamos el tiempo con lo que le falta
            remaining_time[process['pid']] = 0  # El proceso termina
            waiting_time[process['pid']] = current_time - process['arrival_time'] - process['burst_time']  # Calculamos el tiempo de espera

    avg_waiting_time = sum(waiting_time.values()) / len(processes)  # Calculamos el tiempo de espera promedio
    return avg_waiting_time

# Generación de procesos de prueba
def generar_procesos(n):
    procesos = []
    for i in range(n):
        proceso = {
            'pid': i + 1,
            'arrival_time': random.randint(0, 10),  # Tiempo de llegada aleatorio entre 0 y 10
            'burst_time': random.randint(1, 10)    # Tiempo de ejecución aleatorio entre 1 y 10
        }
        procesos.append(proceso)
    return procesos


# Ejecución de los algoritmos
procesos = generar_procesos(5)  # Generamos 5 procesos de prueba
quantum = 3  # Definimos el quantum para Round Robin

# Mostramos los procesos generados
print("Procesos generados:")
for proceso in procesos:
    print(f"PID: {proceso['pid']}, Arrival Time: {proceso['arrival_time']}, Burst Time: {proceso['burst_time']}")

# Ejecutamos y mostramos los resultados de cada algoritmo
print("\nFCFS - Tiempo de espera promedio:", fcfs(procesos))
print("SJF - Tiempo de espera promedio:", sjf(procesos))
print("Round Robin - Tiempo de espera promedio:", round_robin(procesos, quantum))

