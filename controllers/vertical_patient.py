# -*- coding: utf-8 -*-
# from odoo import http

from odoo.http import  Controller, request, route
import json
from datetime import date,datetime
# from odoo.addons.solesco_connector.models.sale_order import sale_order
from odoo import http

import logging


class VerticalPatientController(http.Controller):    
    @http.route('/api/pacientes/consulta', auth='public', type='json', methods=['POST'], csrf=False)
    def pacientes_consulta(self, **post):
        data = json.loads(request.httprequest.data)

        # Crea la orden de venta
        name = data.get('name')

        patient = http.request.env['vertical.patient'].sudo().search([('name', '=', name)])

        if patient:
            return {
                'seq':patient.name, 
                'name': '{} {}'.format(patient.patient_name,patient.patient_last_name),
                'dni': patient.dni,
                'state': patient.state,
            }