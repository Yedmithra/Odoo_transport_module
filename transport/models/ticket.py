from odoo import models, fields

class ticket(models.Model):
    _name = 'car.ticket'
    _description ='gère achat de ticket'
    _rec_name = 'nom_du_client'

    nom_du_client = fields.Many2one('res.partner', string='Nom du client', required=True)
    date = fields.Datetime(string='Date', required=True)
    montant = fields.Float(string='Montant', required=True)
    destination = fields.Char(string='Destination', required=True)
    model_voiture_id = fields.Many2one('car.car', string='Voiture', required=True)
    heure_depart = fields.Datetime(string='Heure de départ', required=True)




