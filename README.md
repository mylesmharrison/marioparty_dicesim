# Mario Party Dice Simulation

Analysis, simulation, and plotting of the dice from Super Mario Party

Backlink: https://mylesharrison.com/2019/01/13/Are-the-Dice-in-Mario-Party-Fair.html

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