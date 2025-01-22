

train_mass = 22680
train_accel = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_cel = f_to_c(100)
print(f100_in_cel)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_far = c_to_f(0)
print(c0_in_far)

def get_force(mass, accel):
  force = mass * accel
  return force

train_force = get_force(train_mass, train_accel)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force")


def get_energy(mass, c = 3 * 10 ** 8):
    energy = mass * c**2
    return energy
  
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, accel, distance):
  work = get_force(mass, accel) * distance
  return work

train_work = get_work(train_mass, train_accel, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

