# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Factor Libre SL (<www.factorlibre.com>).
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
    'name': 'Task HR',
    'version': '1.0',
    'category': 'Project',
    "sequence": 14,
    'complexity': "easy",
    'description': """Task HR
    """,
    'author': 'Factor Libre',
    'website': 'http://factorlibre.com',
    'images': [],
    'depends': ['base','project','hr', 'hr_contract', 'hr_payroll'],
    'init_xml': [],
    'update_xml': [
        'task_employee_workflow.xml',
        'task_view.xml',
        'wizard/multi_task_employee_view.xml'
    ],
    'demo_xml': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
