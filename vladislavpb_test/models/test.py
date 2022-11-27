from odoo import models, fields, api
import random
import json
from time import time, mktime
from datetime import datetime
from odoo.exceptions import ValidationError


class SaleWithTest(models.Model):
    
    _inherit = 'sale.order'

    def _random_num():
        number = round(random.uniform(0, 1000000), 2)
        return "{:,}".format(number)

    sale_test = fields.Char(
                        string='TEST', 
                        required=False, 
                        default=_random_num()
                        )

    @api.onchange('date_order', 'tax_totals_json', 'order_line')
    def _update_test(self):
        now = time()
        for record in self:
            if record.state == 'draft':
                dateunix = mktime(record.date_order.timetuple())
                if abs(now - dateunix) > 3:
                    date = datetime.strftime(record.date_order, '%d/%m/%y %H:%M:%S')
                    total = json.loads(record.tax_totals_json)['amount_total']
                    total = "{:,}".format(total)
                    record.sale_test = f'{total} - {date}'

    @api.constrains('sale_test')
    def _check_len(self):
        for record in self:
            if isinstance(record.sale_test, bool):
                record.sale_test = ''
            if len(record.sale_test) > 50:
                raise ValidationError('Длина текста должна быть меньше 50 символов!')