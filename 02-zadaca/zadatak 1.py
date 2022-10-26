# 1. Kreirajte jednu asinkronu (afun1) i jednu sinkronu (fun2) funkciju, te
# funkciju main. Unutar funkcije main, kreiraju se tri datoteke u radnom
# direktoriju te se nazivi spremaju u listu.
# [“datoteka1”, “datoteka2”, “datoteka3”]
# Nakon toga poziva se afun1 koja uzima parametar lista naziva datoteka.
# Čeka 0.2 sekunde i vraća listu dictionary-a, gdje svaki dictonary sadrži
# naziv datoteke te njenu veličinu u byte-ovima.
# [{“naziv”:“datoteka1”, “velicina”:1212},{“naziv”:“datoteka2”, “velicina”:8912},{“naziv”:“datoteka3”, “velicina”:2212}]
# Odmah nakon afun1, unutar main-a poziva se fun2 koja prima listu naziva
# datoteka. Unutar nje, u svaku datoteku upisuje brojeve od 1 do 10 000.
# Na kraju main-a čeka se rezultat iz afun1 koji se ispisuje u konzolu.
# (Hint: os package)

import asyncio
import glob, os


async def afun1(datoteka):
  await asyncio.sleep(0.2)
  return [{"naziv": x, "velicina": os.path.getsize(x)}  for x in datoteka]

def fun2(datoteka):
    for each in datoteka:
      dat= open(each,"w")
      for i in range(10000):
        dat.write(str(i+1))
        
async def main():

  dat1= open("datoteke/datoteka1.txt","w")
  dat2= open("datoteke/datoteka2.txt","w")
  dat3= open("datoteke/datoteka3.txt","w")
  datlist = []
  
  os.chdir("datoteke/")
  for file in glob.glob("*.txt"):
    datlist.append(file)

  toDoLater = asyncio.create_task(afun1(datlist))
  fun2(datlist)

  await toDoLater
  print(toDoLater.result())
  
asyncio.run(main())