# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenFinance(http.Controller):
#     @http.route('/agrohaven_finance/agrohaven_finance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_finance/agrohaven_finance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_finance.listing', {
#             'root': '/agrohaven_finance/agrohaven_finance',
#             'objects': http.request.env['agrohaven_finance.agrohaven_finance'].search([]),
#         })

#     @http.route('/agrohaven_finance/agrohaven_finance/objects/<model("agrohaven_finance.agrohaven_finance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_finance.object', {
#             'object': obj
#         })