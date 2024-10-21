from odoo import models, fields

class car(models.Model):
    _name = 'car.car'
    _description ='creer les voitures'
    _rec_name = 'fabricant'


    model_voiture = fields.Char(string='Modèle de voiture', required=True)
    fabricant = fields.Char(string='Fabricant', required=True)
    nombre_de_place = fields.Integer(string='Nombre de places', required=True)
    type_de_carburant = fields.Selection([('essence', 'Essence'), ('diesel', 'Diesel')], string='Type de carburant', required=True)
    chauffeur_id = fields.Many2one('hr.employee', string='Chauffeur')

    ticket_ids = fields.One2many('car.ticket', "model_voiture_id")
    voyage_ids = fields.One2many('car.voyage', 'voiture_id')

    def details_chauffeur(self):
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'hr.employee',
                'res_id': self.chauffeur_id.id,
                'view_mode': 'form',
                'target': 'current',
            }

    def change_chauffeur(self):
            return {
                'type': 'ir.actions.act_window',
                'name': 'Changer Chauffeur',
                'res_model': 'change.chauffeur',
                'view_mode': 'form',
                'target': 'new',
            }

