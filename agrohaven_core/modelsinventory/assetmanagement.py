# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Asset Management
class AssetManagement(models.Model):
    _name = 'agrohaven.inventory.assetmanagement'

    # asset management name - will be a calculated field
    name = fields.Char('Asset Management', index=True, required=True, translate=True)