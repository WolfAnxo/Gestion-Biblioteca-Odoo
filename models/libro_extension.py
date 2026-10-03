from odoo import models, fields

class LibroExtension(models.Model):
    _inherit ="biblioteca.libro"
    isbn = fields.Char()