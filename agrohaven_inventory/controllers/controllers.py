# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenInventory(http.Controller):
#     @http.route('/agrohaven_inventory/agrohaven_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_inventory/agrohaven_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_inventory.listing', {
#             'root': '/agrohaven_inventory/agrohaven_inventory',
#             'objects': http.request.env['agrohaven_inventory.agrohaven_inventory'].search([]),
#         })

#     @http.route('/agrohaven_inventory/agrohaven_inventory/objects/<model("agrohaven_inventory.agrohaven_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_inventory.object', {
#             'object': obj
#         })