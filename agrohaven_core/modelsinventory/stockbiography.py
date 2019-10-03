# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Stock Biography
class StockBiography(models.Model):
    _name = 'agrohaven.inventory.stockbiography'

    # stock biography name
    name = fields.Char('Stock Biography', index=True, required=True, translate=True)