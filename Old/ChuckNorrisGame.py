import random
import time

# Define a list of Chuck Norris jokes
chuck_jokes = [
    "Chuck Norris used to beat up his shadow because it was following too close. It now stands 15 feet behind him.",
    "Chuck Norris counted to infinity. Twice.",
    "When Chuck Norris enters a room, he doesn’t turn the lights on. He turns the dark off.",
    "Chuck Norris can divide by zero.",
    "There is no theory of evolution, just a list of creatures Chuck Norris allows to live."
]

# Define insults for hero and enemies
hero_insults = [
    "You bottom dwelling, scum sucking algea eater!!",
    "The mosquitos in my backyard are more of a challenge than you!",
    "Moahahahah! That tickles!!"
]

enemy_insults = [
    "Yippee Ki Yay... mothersucker!!",
    "You honestly thing you can beat me?!? You?!? Moahahahaha!!!",
    "I get more scared of rearanging my sock drawer than the likes of you!!"
]

# Define a class for all characters in the game, including the player and enemies
class GameCharacter:
    def __init__(self, name: str, title: str, health: float, attack: float, block_chance: float):
        self.name = name                    # Name of the character
        self.title = title                  # A short title or description
        self.health = health                # Hit points
        self.attack = attack                # Attack strength
        self.block_chance = block_chance    # Probability to block an attack (0 to 1)
        self.status = "Alive"               # Current status (Alive or Knocked Out)

    def __str__(self):
        # String representation showing health and status
        return f"{self.name} ({self.title}) has {self.health:.1f} HP and is currently {self.status}."

    def attack_target(self, target, is_player=False):
        # Simulate an attack on another character
        hit_roll = random.random()  # Generate random float between 0-1 to determine block

        if hit_roll > target.block_chance:
            # If target fails to block, reduce target's health
            target.health -= self.attack
            print(f"{self.name} hits {target.name} for {self.attack:.1f} damage!")

            # Print a random insult based on who is attacking
            if is_player and target.name != "Chuck Norris":
                print(random.choice(hero_insults))
            elif not is_player and target.name != "Chuck Norris":
                print(random.choice(enemy_insults))

            if target.health <= 0:
                # If target's health reaches zero or below, mark as defeated
                target.status = "You got knocked da fudge out!!!"
                print(f"{target.name} is contemplating life from another realm!")
        else:
            # Target blocks the attack
            print(f"{target.name} blocked {self.name}'s attack! {target.name} saw it coming from a mile away.")

# Ask the player for a custom name (so grammar works better too!)
player_name = input("Enter your hero's name: ")

# Create the main player character
player = GameCharacter(player_name, "The Challenger", 100.0, 20.0, 0.5)  # Out hero's starting stats

# We define all enemy characters (including the final boss... Or the final Chuck)
enemies = [
    GameCharacter("Mat Cauthon", "The Gambler - The Prince of the Ravens", 50, 10, 0.1),
    GameCharacter("Egwene al'Vere", "The Amyrlin Seat", 60, 12, 0.15),
    GameCharacter("Moiraine Damodred", "The Blue Aes Sedai - The Watcher of the Seals", 80, 15, 0.2),
    GameCharacter("Perrin Aybara", "Young Bull - Wolf King", 100, 18, 0.25),
    GameCharacter("Rand al'Thor", "The Dragon Reborn - He Who Comes with the Dawn", 110, 20, 0.3),
    GameCharacter("Chuck Norris", "The man, the myth, the legend", 9999, 999, 1.0)  # Final unbeatable boss
]

# Intro message
print("\nWelcome to the Arena!")
time.sleep(1)
print(f"{player.name}, you will face 5 enemies. After that, you face Chuck Norris himself. Lastly, we will hold your funural")
print("Good luck... you'll need it! And it will not be enough!\n")

# Main battle loop, one enemy at a time
for index, enemy in enumerate(enemies):
    input(f"\nPress Enter to face your next opponent: {enemy.name} - {enemy.title}")
    print(f"A wild {enemy.name} ({enemy.title}) appears! Round 1! FIGHT!!")

    # Fight continues until either the player or the enemy is knocked out
    while player.status == "Alive" and enemy.status == "Alive":
        player.attack_target(enemy, is_player=True)  # Player attacks first
        time.sleep(0.5)

        if enemy.status == "Alive":
            enemy.attack_target(player)  # Enemy counters
            time.sleep(0.5)

    # If player is knocked out, game ends
    if player.status != "Alive":
        print("\nYou have been besten. Oh, the shame. Crawl home and cry!")
        break

    # Ending for for the man, the myth, the legend!
    if enemy.name == "Chuck Norris":
        print("\n" + random.choice(chuck_jokes))
        print("You have been roundhouse-kicked out of existence!")
        break

    # If enemy is defeated (and it's not Chuck... duh), buff the player
    if enemy.name != "Chuck Norris":
        print("You win! Powering up... +10% to attack and block, You gain a +0 to 15% health regeneration!")

        regen_percent = random.uniform(0, 0.15)              # Health gain is random up to 15%
        new_health = player.health * (1 + regen_percent)     # Calculate new health with regen
        player.health = min(new_health, 100.0)               # Cap health at 100%

        player.attack *= 1.10                                # Boost attack by 10%
        player.block_chance = min(player.block_chance * 1.10, 0.9)  # Boost block chance, cap at 90%

        print(f"Health regenerated by {regen_percent*100:.1f}% (capped at 100%)")
        print(player)  # Display updated stats

# Game over message
print("\nThanks for playing. Come back when you’re ready to die at the hands of Chuck Norris again.")
print("If you ever dream about actually beating Chuck Norris... you better wake up and apologize!")
