# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Land use History
class LandUseHistory(models.Model):
    _name = 'agrohaven.inventory.landhistory'

    # landusehistory name - will be a calculated field
    name = fields.Char('Land Use History', index=True, required=True, translate=True)