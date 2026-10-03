from odoo import models, fields
class Editorial(models.Model):
    _name = "biblioteca.editorial"
    _description = "Editorial"
    nombre = fields.Char(required = True)
    _rec_name = "nombre"
    libro_ids = fields.One2many("biblioteca.libro","editorial_id")