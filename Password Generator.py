import time
import random
debug_is_on = False
power = False
pc = True

speak = 'test'




class gen_loader:
    def __init__(self, power):
        self.power = power
        self.york = random.choice([True, False])
        self.old_if_yes = random.randint(1, 60)
        

        if self.york == True:
            self.pc = 'old'
        elif self.york == False or self.power == True:
            self.pc = 'new'


class tetxs():
    def __init__(self, speak= 'test'):
      time.sleep(0.3)
      for l in speak:
          print(l, end="", flush=True)
          time.sleep(0.3)
    print()


outcome = gen_loader(power=True)

def debug():
    debug_is_on = True
    print(outcome.pc)
    print(outcome.old_if_yes)


debug()


if outcome.pc == 'old':
    loader = outcome.old_if_yes
elif debug_is_on == True:
    loader = 1
else:
    loader = 1



print('THE Password Generator')

tetxs('hello')

print("Now sterding", end="", flush=True)
for i in range(4):
    time.sleep(loader)
    print("#", end="", flush=True)
    time.sleep(loader)



for l in "\n oh hellos and welcome":
    print(l, end="", flush=True)
    time.sleep(0.3)
print()
for l in "I am Lockie":
    print(l, end="", flush=True)
    time.sleep(0.3)
print()
time.sleep(0.6)
for l in "Your ai password assistant":
    print(l, end="", flush=True)
    time.sleep(0.3)
print()


