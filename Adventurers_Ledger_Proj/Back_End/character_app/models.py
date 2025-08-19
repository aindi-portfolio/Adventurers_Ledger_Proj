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

class Inventory(models.Model):
    """
    Inventory holds items for a character.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='inventory')
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.IntegerField(default=1)

    def add(self, amount=1):
        if amount < 1:
            raise ValueError("Amount must be at least 1")
        self.quantity += amount
        self.save()
    
    def sub(self, amount=1):
        if amount < 1:
            raise ValueError("Amount must be at least 1")
        if self.quantity - amount < 1:
            return self.delete()
        self.quantity -= amount
        self.save()
    
    def add_item(self, item):
        self.item = item
        self.save()
        self.quantity += 1

    def delete_item(self, item):
        # 1. Check if item (by name) is in the cart
        # 2. If it is, remove it
        if self.item == item:
            self.delete()
        else:
            raise ValueError("Item not found in the cart")


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