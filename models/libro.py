from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Libro(models.Model):
    _name = "biblioteca.libro"
    _description = "Libro"
    titulo = fields.Char(required = True)
    autor = fields.Char()
    paginas = fields.Integer()
    disponible = fields.Boolean(default = True)
    editorial_id = fields.Many2one("biblioteca.editorial")
    generos_ids = fields.Many2many("biblioteca.genero")
    descripcion_paginas = fields.Char(compute ="_compute_descripcion_paginas", store = True)

    def prestar(self):
        self.ensure_one()
        if self.disponible == True:
            self.disponible = False
        else:
            raise UserError("Este libro ya está prestado")

    def devolver(self):
            self.ensure_one()
            if self.disponible == False:
                self.disponible = True
            else:
                raise UserError("Este libro ya esta disponible")

    @api.depends("paginas")
    def _compute_descripcion_paginas(self):
        for libro in self:
            if libro.paginas < 100:
                libro.descripcion_paginas = "Libro corto"
            else:
                libro.descripcion_paginas = "Libro largo"

    @api.constrains("paginas")
    def comprobar_paginas(self):
        for libro in self:
            if libro.paginas <= 0:
                raise ValidationError("El numero de paginas no es correcto")
            