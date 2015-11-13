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

{
    "name" : "Social Cannabis Club",
    "version" : "1.0",
    "author" : "Malabartista GitHub Ltd.",
    "category": '',
    'complexity': "easy",
    'depends': ['web'],
    "description": """
        This module provides the functionality to manage a Social Cannabis Club.
        Includes the functionality to store digital signature image for a record.
        The example can be seen into the Customer's form view where we have added a test field under signature.
    """,
    'data': [
        'views/web_digital_sign_view.xml',
        'partner_view.xml'
    ],
    'website': 'https://www.odoo.com/apps',
    'qweb': ['static/src/xml/digital_sign.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
