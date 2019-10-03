# -*- coding: utf-8 -*-
from odoo import http

# class AgrohavenCore(http.Controller):
#     @http.route('/agrohaven_core/agrohaven_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrohaven_core/agrohaven_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrohaven_core.listing', {
#             'root': '/agrohaven_core/agrohaven_core',
#             'objects': http.request.env['agrohaven_core.agrohaven_core'].search([]),
#         })

#     @http.route('/agrohaven_core/agrohaven_core/objects/<model("agrohaven_core.agrohaven_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrohaven_core.object', {
#             'object': obj
#         })