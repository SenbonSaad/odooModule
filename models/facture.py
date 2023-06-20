from odoo import models, fields

class Facture(models.Model):
    _name = 'gestion.facture'
    _description = 'Modèle de facture'

    facture_id = fields.Char(string="id du facture")
    commande_id = fields.Many2one('gestion.commande', string='Commande')
    numero_facture = fields.Char(string='Numéro de facture', required=True)
    date_facture = fields.Date(string='Date de facture')
    montant_total = fields.Float(string='Montant total')
