#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:38:13 2019

@author: fpalm
"""

#%%

import numpy as np
import matplotlib.pyplot as plt

#%%

market_size = 2000000
unit_revenue = 130
unit_cost = 40
discount_rate = 0.09

rd_cost = 700000000
trials_cost = 150000000
total_costs = rd_cost + trials_cost

growth_factor = np.append(0, np.repeat(0.03, 4))
market_size = market_size * (growth_factor + 1).cumprod()
market_share = 0.08
share_growth_rate = np.append(0, np.repeat(0.2, 4))
share_growth = market_share * (share_growth_rate + 1).cumprod()
sales = market_size * share_growth

annual_revenue = sales * unit_revenue * 12
annual_costs = sales * unit_cost * 12
profit = annual_revenue - annual_costs

net_profit = profit.cumsum() - total_costs

net_pv = np.pv(discount_rate, range(1, 6), 0, -profit).sum() - total_costs
net_pv
#%%

market_size = np.random.normal(2000000, 400000, 10000)
plt.hist(market_size, bins=25)

#%%

rd_cost = np.random.uniform(600000000, 800000000, 10000)
plt.hist(rd_cost, bins=25)

#%%
# lognormal_mean = np.exp(normal_mean + normal_std**2 / 2)
# lognormal_std = np.sqrt(np.exp(normal_std**2) - 1) * np.exp(normal_mean + normal_std**2 / 2)

lognormal_mean = 150000000
lognormal_std = 30000000

normal_std = np.sqrt(np.log(1 + (lognormal_std/lognormal_mean)**2))
normal_mean = np.log(lognormal_mean) - normal_std**2 / 2

trials_cost = np.random.lognormal(normal_mean, normal_std, 10000)
plt.hist(trials_cost, bins=25)

#%%
growth_factor = np.random.triangular(0.02, 0.03, 0.06, 10000)
plt.hist(growth_factor, bins=25)

#%%
share_growth_rate = np.random.triangular(0.15, 0.20, 0.25, 10000)
plt.hist(share_growth_rate, bins=25)
#%%
market_size = np.random.normal(2000000, 400000, (10000, 1))
rd_cost = np.random.uniform(600000000, 800000000, (10000, 1))
trials_cost = np.random.lognormal(normal_mean, normal_std, (10000, 1))
growth_factor = np.random.triangular(0.02, 0.03, 0.06, (10000, 4))
growth_factor = np.hstack((np.zeros((10000, 1)), growth_factor))
share_growth_rate = np.random.triangular(0.15, 0.20, 0.25, (10000, 4))
share_growth_rate = np.hstack((np.zeros((10000, 1)), share_growth_rate))
market_growth = market_size * (growth_factor + 1).cumprod(axis=1)
market_share = np.tile(market_share, (10000, 1))
share_growth = market_share * (share_growth_rate + 1).cumprod(axis=1)
sales = market_growth * share_growth
annual_revenue = sales * unit_revenue * 12
annual_costs = sales * unit_cost * 12
profit = annual_revenue - annual_costs
total_costs = rd_cost + trials_cost
net_profit = profit.cumsum(axis=1) - total_costs
net_pv = np.pv(discount_rate, range(1, 6), 0, -profit).sum(axis=1, keepdims=True) - total_costs
plt.hist(net_pv, bins=25)

(net_pv < 0).mean()