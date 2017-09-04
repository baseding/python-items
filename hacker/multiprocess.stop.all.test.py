import multiprocessing

def myfunction(i, event):
    if not event.is_set():
        print i 
    if i == 20:
        #pass
        event.set()

if __name__ == "__main__":
    p= multiprocessing.Pool(10) 
    m = multiprocessing.Manager()
    event = m.Event()
    for i in range(100):
        p.apply_async(myfunction , (i, event))
    p.close()

    event.wait()  # We'll block here until a worker calls `event.set()`
    p.terminate() # Terminate all processes in the Pool
