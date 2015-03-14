# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Hugo Santos (<http://factorlibre.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
# from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
# import time
#
# from openerp.osv import fields, osv
# from openerp.tools.translate import _
# import openerp.addons.decimal_precision as dp
# import openerp.netsvc
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.one
    @api.depends('order_line.price_subtotal', 'add_disc')
    def _compute_amount(self):
        self.amount_untaxed = sum(line.price_subtotal
                                  for line in self.order_line)
        self.add_disc_amt = self.amount_untaxed * self.add_disc/100
        self.amount_net = self.amount_untaxed - self.add_disc_amt
        self.amount_tax = sum((lambda c: c['total_included'] - c['total'])(
            line.tax_id.compute_all(
            line.price_unit*(1-line.discount/100)*(1-self.add_disc/100),
            line.product_uom_qty,
            product=line.product_id,
            partner=self.partner_id)
        ) for line in self.order_line )
        self.amount_total = self.amount_net + self.amount_tax

    add_disc = fields.Float(
        'Additional Discount(%)',
        default=0.0,
        digits=(4, 2),
        readonly=True,
        states={'draft': [('readonly', False)]})
    add_disc_amt = fields.Float(
        'Additional Disc Amt',
        compute='_compute_amount',
        digits=dp.get_precision('Sale Price'),
        store=True,
        help="The additional discount on untaxed amount.")
    amount_net = fields.Float(
        'Net Amount',
        compute='_compute_amount',
        digits=dp.get_precision('Sale Price'),
        store=True,
        help="The amount after additional discount.")

    # Replace older computing methods.
    amount_tax = fields.Float(
        string='Tax',
        digits=dp.get_precision('Account'),
        store=True,
        readonly=True,
        compute='_compute_amount')
    amount_untaxed = fields.Float(
        string='Subtotal',
        digits=dp.get_precision('Account'),
        store=True,
        readonly=True,
        compute='_compute_amount',
        track_visibility='always')
    amount_total = fields.Float(
        string='Total',
        digits=dp.get_precision('Account'),
        store=True,
        readonly=True,
        compute='_compute_amount')

    @api.v7
    def _make_invoice(self, cr, uid, order, lines, context=None):
        inv_obj = self.pool.get('account.invoice')
        inv_id = super(sale_order, self)._make_invoice(
            cr, uid, order, lines, context=context)
        inv_obj.write(cr, uid, inv_id, {'add_disc': order.add_disc })
        return inv_id

sale_order()
