from django.db import models

class Transaction(models.Model):
    """
    Transaction records the details of an item purchase.
    """
    player = models.ForeignKey('player_app.Player', on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=50, choices=[('purchase', 'Purchase'), ('sale', 'Sale')], default='purchase') # Will need addtional integration
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='transactions')
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)