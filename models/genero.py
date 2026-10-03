from odoo import models, fields

class Genero(models.Model):
    _name = "biblioteca.genero"
    _description = "Género"
    nombre = fields.Char(required = True)
    _rec_name = "nombre"
