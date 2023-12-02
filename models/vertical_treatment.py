# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.http import request
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from num2words import num2words

class VerticalTreatment(models.Model):
    _name="vertical.treatment"
    _description="Vertical Treatment"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin'] #Tacker para auditoría
    _order='name desc'


    company_id = fields.Many2one(
        'res.company', string='Company', copy=False, required=True,
        store=True, readonly=False,
        default=lambda self: self.env.company,
        states={'draft': [('readonly', False)], 'payed': [('readonly', False)]})


    name = fields.Char(string="Tratamiento", states={'draft': [('readonly', False)]},required=True)
    code = fields.Char(string="Código", states={'draft': [('readonly', False)]}, equired=True)
    
    partner_id = fields.Many2one('res.partner', string="Medico", states={'draft': [('readonly', False)]},required=True)


    @api.constrains('code')
    def _check_code_sequence(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError("El código no puede contener la secuencia '026'.")
