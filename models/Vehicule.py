from odoo import models, fields

class Vehicule(models.Model):
    _name = 'gestion.vehicule'
    _description = 'Modèle de véhicule'

    name = fields.Char(string='Nom', required=True)
    marque = fields.Char(string='Marque')
    immatriculation = fields.Char(string='Immatriculation')
    annee_fabrication = fields.Integer(string="Année de fabrication")
