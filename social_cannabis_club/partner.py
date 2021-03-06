# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#    Copyright (C) 2015 Malabartista GitHub
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

from openerp import models, fields, api

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dni= fields.Char(string='DNI')
    socio_id= fields.Integer(string='Num Socio')
    discharge_date= fields.Date(string='Fecha de Alta')
    debts= fields.Float(string='Deudas')
    signature= fields.Html(string='Signature')
    signature_image= fields.Binary(string='Signature')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: