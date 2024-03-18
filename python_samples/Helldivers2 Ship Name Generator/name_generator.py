import tkinter as tk
import random

prefix = ['Adjudicator', 'Advocate', 'Aegis', 'Agent', 'Arbiter', 'Banner', 'Beacon', 'Blade', 'Bringer', 'Champion', 'Citizen', 'Claw', 
          'Colossus', 'Comptroller', 'Courier', 'Custodian', 'Dawn', 'Defender', 'Diamond', 'Distributor', 'Dream', 'Elected Representative', 
          'Emperor', 'Executor', 'Eye', 'Father', 'Fist', 'Flame', 'Force', 'Forerunner', 'Founding Father', 'Gauntlet', 'Giant', 'Guardian', 
          'Halo', 'Hammer', 'Harbinger', 'Herald', 'Judge', 'Keeper', 'King', 'Knight', 'Lady', 'Legislator', 'Leviathan', 'Light', 
          'Lord', 'Magistrate', 'Marshal', 'Martyr', 'Mirror', 'Mother', 'Octagon', 'Ombudsman', 'Panther', 'Paragon', 'Patriot', 'Pledge',
          'Power', 'Precursor', 'Pride', 'Prince', 'Princess', 'Progentitor', 'Prophet', 'Protector', 'Purveyor', 'Queen', 'Ranger', 'Reign', 
          'Representative', 'Senator', 'Sentinel', 'Shield', 'Soldier', 'Song', 'Soul', 'Sovereign', 'Spear', 'Stallion', 'Star', 
          'Steward', 'Superintendent', 'Sword', 'Titan', 'Triumph', 'Warrior', 'Whisper', 'Will', 'Wings'
          ]

suffix = ['Allegiance', 'Audacity', 'Authority', 'Battle', 'Benevolence', 'Conquest', 'Conviction', 'Conviviality', 'Courage', 'Dawn', 
          'Democracy', 'Destiny', 'Destruction', 'Determination', 'Equality', 'Eternity', 'Family Values', 'Fortitude', 'Freedom', 
          'Glory', 'Gold', 'Honor', 'Humankind', 'Independence', 'Individual Merit', 'Integrity', 'Iron', 'Judgment', 'Justice', 'Law',
          'Liberty', 'Mercy', 'Midnight', 'Morality', 'Morning', 'Opportunity', 'Patriotism', 'Peace', 'Perseverance', 'Pride', 
          'Redemption', 'Science', 'Self-Determination', 'Selfless Service', 'Serenity', 'Starlight', 'Steel', 'Super Earth', 'Supremacy',
          'the Constitution', 'the People', 'the Regime', 'the Stars', 'the State', 'Truth', 'Twilight', 'Victory', 'Vigilance', 'War',
          'Wrath'
          ]

def on_button_click():
    label2.config(text=f"{random.choice(prefix)} " + "of " + f"{random.choice(suffix)}")

# Create the main application window
app = tk.Tk()
app.title("Helldivers Ship Name Generator")  # Change the window title

# Set the default size of the window
app.geometry("400x200")  # Width x Height

# Create a button widget
button = tk.Button(app, text="Generate Name", command=on_button_click)  # Change the button text
button.pack()

# Create a label to make space below the Button
label1 = tk.Label(app, text="")
label1.pack()

# Create a label widget
label2 = tk.Label(app, text="")
label2.pack()

# Run the application
app.mainloop()
