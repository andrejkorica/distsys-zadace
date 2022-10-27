#Kreirajte dvije asinkrone funkcije (afunc1, afunc2) i funkciju main. Untutar funkcije main 
#pozivaju se obje funkcije jedna za drugom. Afunc1
#kreira 10 Normalnih distribucija s 1M sample-ova i nakon svake čeka 0.9
#sekundi. Afunc2 prati iskorištenost CPU-a u vremenskom razmaku od 10
#sekundi. Na kraju funkcije main, čeka se rezultat afunc2 te se u konzolu
#ispisuje iskorištenost CPU-a.
#(Hint: numpy, psutils package)
#Iskorištenost CPU u 10 sekundi iznosi : 3.8
import asyncio as ai
import numpy as np
import psutil as ps

async def afun1():
  
  lista = []
  for i in range(10):
    lista.append(np.random.normal(0, 0.1, 1000000))
    await ai.sleep(0.9)
  return lista

async def afun2():
  return print("CPU:", ps.cpu_percent(10))

async def main():
  nekitask1 = ai.create_task(afun1())
  nekitask = ai.create_task(afun2())
  await nekitask1
  await nekitask
  nekitask.result()
ai.run(main())