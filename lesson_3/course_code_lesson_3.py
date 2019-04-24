#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

content = pd.read_csv('D:\\code\\data\\titanic\\train.csv ')
content = content.dropna()
age_with_fares = content[
    (content['Age'] > 22) & (content['Fare'] < 400 ) & (content['Fare'] > 130)
]

sub_fare = age_with_fares['Fare']
sub_age = age_with_fares['Age']

# plt.scatter(sub_age,sub_fare)

def func(age,k,b):
    return k*age + b

def loss(y,yhat):
    """

    :param y:    the read fares
    :param yhat:  the estimated fares
    :return:   how good is the estimateed fares
    """
    return np.mean(np.abs(y-yhat))


change_directions = [
    #(k,b)
    (+1,-1),
    (+1,+1),
    (-1,+1),
    (-1,-1)
]

k_hat = random.random() * 20 - 10
b_hat = random.random() * 20 - 10
loop_times = 1000

min_error_rate = float('inf')
best_k,best_b = k_hat,b_hat
best_direction = None

#生成一个 (-1,1)的随机数
def step():
    return random.random()*2 -1

losses = []
direction = random.choice(change_directions)
while loop_times >0:
    k_delta_direction,b_delta_direction = direction

    k_delta = k_delta_direction * step()
    b_delta = b_delta_direction * step()

    new_k = best_k + k_delta
    new_b = best_b + b_delta

    # k_hat = random.random() * 20 - 10
    # b_hat = random.random() * 20  - 10
    estimated_fares = func(sub_age,new_k,new_b)
    error_rate = loss(y=sub_fare,yhat=estimated_fares)
    if error_rate <min_error_rate:
        min_error_rate = error_rate
        best_k,best_b = k_hat,b_hat

        direction = (k_delta_direction,b_delta_direction)

        losses.append(min_error_rate)
        print('loop == {}'.format(1000-loop_times))
        print('f(age) = {}*age+{},with error rate"{}'.format(best_k,best_b,min_error_rate))
    else:
        direction = random.choice(change_directions)
    loop_times -= 1

# plt.scatter(sub_age,sub_fare)
# plt.plot(sub_age,func(sub_age,best_k,best_b),c='r')
# # plt.plot(range(len(losses)),losses)
# plt.show()
"""

while loop_times > 0:

    k_delta = -1 * learing_rate * derivate_k(sub_fare, func(sub_age, k_hat, b_hat), sub_age)
    b_delta = -1 * learing_rate * derivate_b(sub_fare, func(sub_age, k_hat, b_hat))

    # k_delta_direction, b_delta_direction = direction
    #
    # k_delta = k_delta_direction * step()
    # b_delta = b_delta_direction * step()
    #
    # new_k = best_k + k_delta
    # new_b = best_b + b_delta

    k_hat += k_delta
    b_hat += b_delta

    estimated_fares = func(sub_age, k_hat, b_hat)
    error_rate = loss(y=sub_fare, yhat=estimated_fares)

    # if error_rate < min_error_rate:
    #     min_error_rate = error_rate
    #     best_k, best_b = new_k, new_b
        # best_k, best_b = k_hat, b_hat

        # direction = (k_delta_direction, b_delta_direction)

        # print(min_error_rate)
    print('loop == {}'.format(loop_times))
        # losses.append(min_error_rate)
    print('f(age) = {} * age + {}, with error rate: {}'.format(best_k, best_b, error_rate))
    # else:
    #     direction = random.choice(list(set(change_directions) - {(k_delta_direction, b_delta_direction)}))

    losses.append(error_rate)

    loop_times -= 1
"""



"""
min_error_rate = float('inf')

loop_times = 10000

losses = []

change_directions = [
    # (k, b)
    (+1, -1), # k increase, b decrease
    (+1, +1),
    (-1, +1),
    (-1, -1)  # k decrease, b decrease
]

k_hat = random.random() * 20 - 10
b_hat = random.random() * 20 - 10

best_k, best_b = k_hat, b_hat

best_direction = None


def step(): return random.random() * 1


direction = random.choice(change_directions)


def derivate_k(y, yhat, x):
    abs_values = [1 if (y_i - yhat_i) > 0 else -1 for y_i, yhat_i in zip(y, yhat)]

    return np.mean([a * -x_i for a, x_i in zip(abs_values, x)])


def derivate_b(y, yhat):
    abs_values = [1 if (y_i - yhat_i) > 0 else -1 for y_i, yhat_i in zip(y, yhat)]
    return np.mean([a * -1 for a in abs_values])


learing_rate = 1e-1


while loop_times > 0:

    k_delta = -1 * learing_rate * derivate_k(sub_fare, func(sub_age, k_hat, b_hat), sub_age)
    b_delta = -1 * learing_rate * derivate_b(sub_fare, func(sub_age, k_hat, b_hat))

    # k_delta_direction, b_delta_direction = direction
    #
    # k_delta = k_delta_direction * step()
    # b_delta = b_delta_direction * step()
    #
    # new_k = best_k + k_delta
    # new_b = best_b + b_delta

    k_hat += k_delta
    b_hat += b_delta

    estimated_fares = func(sub_age, k_hat, b_hat)
    error_rate = loss(y=sub_fare, yhat=estimated_fares)

    # if error_rate < min_error_rate:
    #     min_error_rate = error_rate
    #     best_k, best_b = new_k, new_b
        # best_k, best_b = k_hat, b_hat

        # direction = (k_delta_direction, b_delta_direction)

        # print(min_error_rate)
    print('loop == {}'.format(loop_times))
        # losses.append(min_error_rate)
    print('f(age) = {} * age + {}, with error rate: {}'.format(best_k, best_b, error_rate))
    # else:
    #     direction = random.choice(list(set(change_directions) - {(k_delta_direction, b_delta_direction)}))

    losses.append(error_rate)

    loop_times -= 1
"""

# plt.scatter(sub_age, sub_fare)
# plt.plot(sub_age, func(sub_age, best_k, best_b), c='r')
# plt.plot(sub_age, func(sub_age, k_hat, b_hat), c='r')
# plt.show()

# plt.plot(range(len(losses)), losses)
# plt.show()





















