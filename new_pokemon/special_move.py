import random

class SpecialMove:
    def __init__(self, name, damage, accuracy, effect=None):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.effect = effect

    def apply_effect(self, target):
        if self.effect and random.random() < self.effect.get('chance', 1.0):
            status = self.effect.get('status')
            duration = self.effect.get('duration', 3)  # Default duration of 3 turns
            if status:
                target.add_status_effect(status, duration)
                print(f"{target.name} is affected by {status} for {duration} turns!")
