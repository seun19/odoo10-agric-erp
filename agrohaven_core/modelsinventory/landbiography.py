# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Land Biography
class LandBiography(models.Model):
    _name = 'agrohaven.inventory.landbiography'

    # land biography name
    name = fields.Char('Land Biography', index=True, required=True, translate=True)
