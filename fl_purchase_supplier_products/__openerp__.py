# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Factor Libre.
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
    'name': 'Purchase Filter Supplier Products',
    'version': '0.1',
    'category': 'Purchase Management',
    'description': """In Purchases shows only the products of the selected supplier""",
    'author': 'Factor Libre',
    'maintainer': 'Factor Libre',
    'website': 'http://www.factorlibre.com',
    'depends': ['base', 'product', 'purchase'],
    'init_xml': [],
    'update_xml': [
        'product_view.xml',
        'purchase_view.xml',
    ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
