# -*- encoding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.one
    @api.depends('invoice_line.price_subtotal', 'tax_line.amount', 'add_disc')
    def _compute_amount(self):
        precision = self.env['decimal.precision'].precision_get('Account')
        self.amount_untaxed = sum(line.price_subtotal
                                  for line in self.invoice_line)
        self.add_disc_amt = round(
            self.amount_untaxed * self.add_disc/100,
            precision)
        self.amount_net = self.amount_untaxed - self.add_disc_amt
        self.amount_tax = round(
            sum(line.amount for line in self.tax_line) *
            (1 - self.add_disc/100),
            precision)
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
account_invoice()


class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'

    @api.model
    def move_line_get_item(self, line):
        precision = self.env['decimal.precision'].precision_get('Account')
        r = super(account_invoice_line, self).move_line_get_item(line)
        r['price'] = round(
            r['price'] * ((100 - line.invoice_id.add_disc)/100.0),
            precision)
        return r
account_invoice_line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
