# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\users\vladislav\documents\computer_science\odoo_application\odoo_module\vladislavpb(models.Model):
#     _name = 'c:\users\vladislav\documents\computer_science\odoo_application\odoo_module\vladislavpb.c:\users\vladislav\documents\computer_science\odoo_application\odoo_module\vladislavpb'
#     _description = 'c:\users\vladislav\documents\computer_science\odoo_application\odoo_module\vladislavpb.c:\users\vladislav\documents\computer_science\odoo_application\odoo_module\vladislavpb'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
