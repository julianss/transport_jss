# -*- coding: utf-8 -*-

{
    'name': 'Cotización de Transporte',
    'category': 'Warehouse',
    'summary': 'Crear información de rutas y cotizarla',
    'author': 'JSS',
    'website': '',
    'version': '1.0',
    'description':"""
""",
    'images': [],
    'depends': ['sale',
                'sales_team',
                'fleet',
                'hr'
                ],
    'data': [
        'views/transport_view.xml',
        'security/ir.model.access.csv',
        'data/transport_sequence.xml',
        'views/picking_transport_info_view.xml',
        'views/route_location_view.xml',
        'views/fleet_view.xml',
        'views/product_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
