from odoo import models, fields
from odoo import api
from datetime import datetime

class voyage(models.Model):
    _name = 'car.voyage'
    _description ='renseigne sur voyage'
    _rec_name = 'destination'

    voiture_id = fields.Many2one('car.car', string='Voiture', required=True)
    lieu_depart = fields.Char(string='Lieu de départ', required=True)
    destination = fields.Char(string='Destination', required=True)
    date_depart = fields.Datetime(string='Date de départ', required=True)
    date_arrivee = fields.Datetime(string='Date d\'arrivée', required=True)
    duree_voyage = fields.Char(string='Durée du voyage', compute='_compute_duree_voyage', store=True)
    #nombre_de_place = fields.Integer(string='Nombre de places', related='voiture_id.nombre_de_place', readonly=True, store=True)
    nombre_de_place = fields.Integer(string='Nombre de places', compute='_compute_nombre_de_place')

    @api.depends('date_depart', 'date_arrivee')
    def _compute_duree_voyage(self):
        for voyage in self:
            if voyage.date_depart and voyage.date_arrivee:
                date_depart = fields.Datetime.from_string(voyage.date_depart)
                date_arrivee = fields.Datetime.from_string(voyage.date_arrivee)
                duree = date_arrivee - date_depart
                #print(duree)
                #voyage.duree_voyage = duree.total_seconds() / 3600
                duree_en_secondes = duree.total_seconds()
                print("duree_en_secondes", duree_en_secondes)
                jour, re = divmod(duree_en_secondes, 86400)
                heures, reste = divmod(re, 3600)
                minutes, secondes = divmod(reste, 60)
                temps= f"{int(jour)} jours,{int(heures)} heures, {int(minutes)} minutes, {int(secondes)} secondes"
                voyage.duree_voyage = temps
                print(voyage.duree_voyage)
            else:
                voyage.duree_voyage = 0

    @api.depends('voiture_id')
    def _compute_nombre_de_place(self):
            for voyage in self:
                voyage.nombre_de_place = voyage.voiture_id.nombre_de_place
