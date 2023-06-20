from odoo import models, fields

class Paiement(models.Model):
    _name = 'gestion.paiement'
    _description = 'Modèle de paiement'

    client_name = fields.Many2one('gestion.commande', string='commande')
    montant = fields.Float(string='Montant')
    date_paiement = fields.Date(string='Date du paiement')
    facture_id = fields.Many2one('gestion.facture', string='Facture')
