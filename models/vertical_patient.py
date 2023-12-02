# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.http import request
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from num2words import num2words

class VerticalPatient(models.Model):
    _name="vertical.patient"
    _description="Vertical Patient"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin'] #Tacker para auditoría
    _order='name desc'


    name = fields.Char(string='Secuencia', 
                       required=True, copy=False, readonly=True, 
                       index=True, 
                       default=lambda self: _('New'))

    company_id = fields.Many2one(
        'res.company', string='Company', copy=False, required=True,
        store=True, readonly=False,
        default=lambda self: self.env.company,
        states={'draft': [('readonly', False)], 'payed': [('readonly', False)]})


    patient_name = fields.Char(string="Nombre", states={'draft': [('readonly', False)]},)
    patient_last_name = fields.Char(string="Apellido", states={'draft': [('readonly', False)]},)
    
    dni = fields.Integer(string="DNI", states={'draft': [('readonly', False)]})


    discharge_date = fields.Datetime("Fecha-Hora de Alta", states={'draft': [('readonly', False)]},)


    state = fields.Selection([
            ('draft', 'Borrador'),
            ('discharge', 'Alta'),
            ('release', 'Baja'),],
            string='State', index=True, readonly=True, copy=False,
            default='draft', tracking=True, store=True)


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vertical.patient') or 'New'
            result = super(VerticalPatient, self).create(vals)
            return result
            
    def sent_to_draft(self):
        for rec in self:
            rec.write({'state':'draft'})

    def action_discharge(self):
        for rec in self:
            rec.write({'state':'discharge'})

    def action_release(self):
        for rec in self:
            rec.write({'state':'release'})