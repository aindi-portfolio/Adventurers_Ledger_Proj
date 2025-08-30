from django.db import models

class Character(models.Model):
    """
    character gets created when a user signs up.
    """
    user_account = models.ForeignKey(
        "user_app.UserAccount", 
        on_delete=models.CASCADE, 
        related_name='character', default=None
    )
    name = models.CharField(max_length=100, unique=True)
    character_class = models.CharField(max_length=50, default='Adventurer')  # Default class can be changed later
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    gold = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        print(f"""
              Character Name: {self.name}\n
              Character Level: {self.level}\n
              Character Experience: {self.experience}\n
              Character Health: {self.health}\n
              Character Gold: {self.gold}""")

    def __str__(self):
        return f"{self.name} (Level {self.level} {self.character_class})"

class Inventory(models.Model):
    """
    Inventory holds items for a character.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='inventory')
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.IntegerField(default=1)

    @classmethod
    def add_item_to_character(cls, character, item, quantity=1):
        """
        Add an item to a character's inventory or increase quantity if it already exists.
        """
        inventory_entry, created = cls.objects.get_or_create(
            character=character,
            item=item,
            defaults={'quantity': 0}
        )
        inventory_entry.add(quantity)
        return inventory_entry

    def __str__(self):
        return f"{self.character.name}'s {self.item.name} x{self.quantity}"

    def add(self, amount=1):
        # Increase the quantity of this inventory item
        if amount < 1:
            raise ValueError("Amount must be at least 1")
        self.quantity += amount
        self.save()
    
    def sub(self, amount=1):
        if amount < 1:
            raise ValueError("Amount must be at least 1")
        if self.quantity - amount < 1:
            print(f"Deleting inventory entry for {self.item.name}")
            return self.delete()
        self.quantity -= amount
        self.save()

    
    def add_item(self, item):
        # This method should not be used on existing inventory instances
        # Use get_or_create to add items to inventory instead
        raise NotImplementedError("Use Inventory.objects.get_or_create() to add new items to inventory")

    def delete_item(self):
        # Remove this inventory entry completely
        self.delete()


class Transaction(models.Model):
    """
    Transaction records the details of an item purchase.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=50, choices=[('purchase', 'Purchase'), ('sale', 'Sale')], default='purchase') # Will need addtional integration
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='transactions')
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.character.name} {self.transaction_type} {self.quantity}x {self.item.name} for {self.total_price}"