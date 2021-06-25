# -*- coding: utf-8 -*-
# from odoo import http


# class KzmDigestMail(http.Controller):
#     @http.route('/kzm_digest_mail/kzm_digest_mail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kzm_digest_mail/kzm_digest_mail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kzm_digest_mail.listing', {
#             'root': '/kzm_digest_mail/kzm_digest_mail',
#             'objects': http.request.env['kzm_digest_mail.kzm_digest_mail'].search([]),
#         })

#     @http.route('/kzm_digest_mail/kzm_digest_mail/objects/<model("kzm_digest_mail.kzm_digest_mail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kzm_digest_mail.object', {
#             'object': obj
#         })
