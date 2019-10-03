# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Traceability
class Traceability(models.Model):
    _name = 'agrohaven.inventory.traceability'

    # traceability name - will be a calculated field
    name = fields.Char('Asset Management', index=True, required=True, translate=True)