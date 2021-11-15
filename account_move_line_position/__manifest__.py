{
    'name': "Account Move Line Position",

    'summary': """
        Get line position from purchase or sale order.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Accounting',
    'version': '14.0.1.1.0',
    'license': 'AGPL-3',
    
    'depends': ['account', 'sale_order_line_position', 'purchase_order_line_position'],

    'data': [
        'views/view_move_form.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}