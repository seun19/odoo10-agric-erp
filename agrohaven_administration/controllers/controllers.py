# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenAdministration(http.Controller):
#     @http.route('/agrohaven_administration/agrohaven_administration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_administration/agrohaven_administration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_administration.listing', {
#             'root': '/agrohaven_administration/agrohaven_administration',
#             'objects': http.request.env['agrohaven_administration.agrohaven_administration'].search([]),
#         })

#     @http.route('/agrohaven_administration/agrohaven_administration/objects/<model("agrohaven_administration.agrohaven_administration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_administration.object', {
#             'object': obj
#         })