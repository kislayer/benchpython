import time
from multiprocessing import Process, Manager

def checkprime(number):
    for prime in primes:
        if number % prime == 0:
            return False
    primes.append(number)
    print(str(number) + " is prime" )
    return True

def checkmaybeprime(number,maybeprime,primes):
    for prime in primes:
        if number % prime == 0:
            return False
    maybeprime.append(number)
    print(str(number) + " maybe prime" )
    return True

if __name__ ==  '__main__':
    with Manager() as manager:
        start = time.perf_counter()

        primes = [2,3,5]

        ##Fills first 1000 prime numbers
        for x in range(2, 2000):
            checkprime(x)

        for loops in range(1,10):

            maybeprime = manager.list()
            jobs = []

            for x in range(2000*loops, (3000*loops)):
                job = Process(target=checkmaybeprime, args=[x, maybeprime, primes],)
                jobs.append(job)
    
            for job in jobs:
                job.start()

            for job in jobs:
                job.join()

            for number in maybeprime:
                checkprime(number)

        print (primes)

        finish = time.perf_counter()

        print(f'Fisished in {round (finish - start,2)}')