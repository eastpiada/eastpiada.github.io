import koios_python
import os
import json
import pandas as pd

# create a koios_python instance and set the network
kp = koios_python.URLs(network='mainnet')

# get tip and make into a dataframe
tip = pd.DataFrame(kp.get_tip(), index=[0])

# get current epoch number
epoch = tip.epoch_no[0]

# Pool_bech32_ID
piada = 'pool1hrv8gtrm0dgjg6zyss5uwa4nkruzfnh5vrdkr2sayj7x2nw6mjc'

piada_history = pd.DataFrame(kp.get_pool_history(piada))

piada_info = pd.DataFrame(kp.get_pool_info(piada))

# Need pledge, live stake, live delegators, margin, block count, past 10 epoch ros, epoch_current then put it into a json file
pledge = int(piada_info.pledge[0])/1000000
total_delegated = int(piada_info.live_stake[0])/1000000
number_of_delegators = int(piada_info.live_delegators[0])
pool_fee = int(piada_info.margin[0]) * 100
block_count = int(piada_info.block_count[0])
epoch = int(tip.epoch_no[0])
delegate_rewards = piada_history.deleg_rewards.astype(int).sum() / 1000000
ten_epoch_ros = piada_history.epoch_ros.astype(int).tail(10).mean()

# lets make the some of the numbers look nice and convert to strings to look like this "80,000" without the ending .0
pledge = "{:,}".format(pledge).replace('.', '')
delegate_rewards = "{:,}".format(delegate_rewards).replace('.', '')
total_delegated = "{:,}".format(total_delegated).replace('.', '')

# now lets get all this data into a json file from a dataframe

pool_data = pd.DataFrame({'pledge': [pledge], 'total_delegated': [total_delegated], 'number_of_delegators': [number_of_delegators], 
                          'pool_fee': [pool_fee], 'block_count': [block_count], 'epoch': [epoch], 'delegate_rewards': [delegate_rewards], 
                          'ten_epoch_ros': [ten_epoch_ros]})

pool_data.to_json('poolData.json', orient='records')