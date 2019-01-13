# Mario Party Dice Simulation

Analysis, simulation, and plotting of the dice from Super Mario Party

@author: Myles Harrison  
@email: [myles at mylesharrison dot com](mailto:myles@mylesharrison.com)  
@web: Backlink here: https://everydayanalytics.ca/2019/01/are-the-dice-in-mario-party-fair.html

Batch plotting:
```python
python mario_party_dicesim.py
```

Interactive use:
```python
from mario_party_dicesim import *
rolls, rolls_avg = simulate_rolls(dice_dict['Mario'], 1000)
plot_rolls(rolls, rolls_avg, 'Mario')
plt.show()
```