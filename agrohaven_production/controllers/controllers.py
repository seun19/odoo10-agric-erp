# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenProduction(http.Controller):
#     @http.route('/agrohaven_production/agrohaven_production/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_production/agrohaven_production/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_production.listing', {
#             'root': '/agrohaven_production/agrohaven_production',
#             'objects': http.request.env['agrohaven_production.agrohaven_production'].search([]),
#         })

#     @http.route('/agrohaven_production/agrohaven_production/objects/<model("agrohaven_production.agrohaven_production"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_production.object', {
#             'object': obj
#         })