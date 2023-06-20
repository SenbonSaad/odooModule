from odoo import models, fields

class commande(models.Model):
    _name = 'gestion.commande'
    _description = 'Commande Model'
    commande_id = fields.Char(string="id du commande")
    client_name = fields.Char(string='Client Name')
    pickup_address = fields.Char(string='Pickup Address')
    delivery_address = fields.Char(string='Delivery Address')
    delivery_date = fields.Date(string='Delivery Date')
    amount = fields.Float(string='Amount')
