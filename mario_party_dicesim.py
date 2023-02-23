# Super Mario Party Dice Simulation
# ---------------------------------
# Myles Harrison
# http://www.mylesharrison.com

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dice_dict = {
	'Boo': [0,0,5,5,7,7],
	'Bowser': [0,0,1,8,9,10],
	'Bowser Jr.': [1,1,1,4,4,9],
	'Daisy': [3,3,3,3,4,4],
	'Diddy Kong': [0,0,0,7,7,7],
	'Donkey Kong': [0,0,0,0,10,10],
	'Dry Bones': [1,1,1,6,6,6],
	'Goomba': [0,0,3,4,5,6],
	'Hammer Bro': [0,1,1,5,5,5],
	'Koopa': [1,1,2,3,3,10],
	'Luigi': [1,1,1,5,6,7],
	'Mario': [1,3,3,3,5,6],
	'Monty Mole': [0,2,3,4,5,6],
	'Peach': [0,2,4,4,4,6],
	'Pom Pom': [0,3,3,3,3,8],
	'Rosalina': [0,0,2,3,4,8],
	'Shy Guy': [0,4,4,4,4,4],
	'Waluigi': [0,1,3,5,5,7],
	'Wario': [6,6,6,6,0,0],
	'Yoshi': [0,1,3,3,5,7],
	'Standard': [1,2,3,4,5,6]
}

def simulate_rolls(dice, n):
	roll_index = np.arange(0, n, 1) + 1 # Generate the roll index
	roll_faces = np.random.randint(0, 6, n) # Generate the random rolls (face #)
	f = np.vectorize(lambda x: dice[x]) # Generate a vectorized numpy function for mapping the faces to the different dice
	rolls = f(roll_faces) # Apply to get all the random dice rolls
	roll_avg = np.cumsum(rolls)/roll_index.astype(float) # Calculate the running average
	return rolls, roll_avg

def plot_rolls(rolls, rolls_avg, label):
	# Find uniques and counts (better than histogram as this is categorical / discrete values)
	roll_values, count = np.unique(rolls, return_counts=True)

	fig = plt.figure()
	# Top plot
	ax = plt.subplot(2,1,1)
	ax.bar(roll_values, count)
	ax.set_title(label)
	plt.xlim(-0.5, 10.5)
	plt.xticks(range(0, 11, 1))
	plt.xlabel('Roll Value')
	plt.ylabel('Count')
	# Bottom plot
	ax = plt.subplot(2,1,2)
	ax.plot(rolls_avg)
	plt.xlabel('Roll #')
	plt.ylabel('Running Average')
	plt.tight_layout()
	# Save
	plt.savefig('./output/'+label+'.png')
	plt.close()

if __name__ == "__main__":

	# Iterate over each of the dice, simulate 1000 rolls and plot
	for (character, dice) in dice_dict.iteritems():
		rolls, rolls_avg = simulate_rolls(dice, 1000)
		plot_rolls(rolls, rolls_avg, character)

