from odoo import fields, models
import random


class SaleWithTest(models.Model):
    _inherit = 'sale.order'

    Test = fields.Char('Test', computed='random_numb')

    def random_numb():
        return str(random.uniform(a=-1000000, b=100000))
