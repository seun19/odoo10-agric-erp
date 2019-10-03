# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Inventory Tracker
class InventoryTracker(models.Model):
    _name = 'agrohaven.inventory.inventorytracker'

    # inventory tracker name - will be a calculated field
    name = fields.Char('Inventory Tracker', index=True, required=True, translate=True)
