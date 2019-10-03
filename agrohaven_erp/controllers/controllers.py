# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenErp(http.Controller):
#     @http.route('/agrohaven_erp/agrohaven_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_erp/agrohaven_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_erp.listing', {
#             'root': '/agrohaven_erp/agrohaven_erp',
#             'objects': http.request.env['agrohaven_erp.agrohaven_erp'].search([]),
#         })

#     @http.route('/agrohaven_erp/agrohaven_erp/objects/<model("agrohaven_erp.agrohaven_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_erp.object', {
#             'object': obj
#         })