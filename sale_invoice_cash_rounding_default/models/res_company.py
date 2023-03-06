from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_cash_rounding_id = fields.Many2one('account.cash.rounding', string='Default Cash Rounding Method')