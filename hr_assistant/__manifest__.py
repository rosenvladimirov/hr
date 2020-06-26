# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "HR Sale person assistant",
    "version": "11.0.1.0",
    "author": "Rosen Vladimirov, BioPrint Ltd.",
    'category': 'Sale',
    "website": "https://github.com/rosenvladimirov/hr",
    "description": """
This module add filed for assistant to help Sales person
    """,
    'depends': [
        'sale',
    ],
    "demo": [],
    "data": [
        'views/sale_views.xml',
    ],
    "license": "AGPL-3",
    "installable": True,
}
