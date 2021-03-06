# -*- encoding: utf-8 -*-
{
    'name': 'Account Bank Statement Import',
    'category': 'Accounting & Finance',
    'version': '1.0',
    'author': 'OpenERP SA,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/bank-statement-import',
    'depends': ['account'],
    'data': [
        'account_bank_statement_import_view.xml',
    ],
    'demo': [
        'demo/fiscalyear_period.xml',
        'demo/partner_bank.xml',
    ],
    'auto_install': False,
    'installable': True,
}
