from odoo import models, fields, api

class ChangeChauffeur(models.TransientModel):
    _name = 'change.chauffeur'
    _description = 'Assistant de changement de chauffeur'

    nouveau_chauffeur = fields.Many2one('hr.employee', string='Nouveau Chauffeur', required=True)

    def fchange_chauffeur(self):
        active_car = self.env['car.car'].browse(self.env.context.get('active_id'))
        if active_car:
            active_car.chauffeur_id = self.nouveau_chauffeur