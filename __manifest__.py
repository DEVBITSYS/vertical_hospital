# -*- coding: utf-8 -*-
{
    'name': "Vertical Hospital",
    'description': """
        Este es un Test de Desarrollador de aplicación para Quilsoft.
    """,
    'author': "Jhayr Marin",
    
    'depends': ['base','mail','portal'],
    # 'qweb': ['static/src/xml/*.xml'],  # Nueva línea para agregar archivos qweb
    'application': True,  # Nueva línea para configurar como aplicación
    'installable': True,
    'auto_install': False,
    
    'version': '16.0',
    'license': 'LGPL-3',
    'support': 'jhayr.marin95@gmail.com',
    'website': "https://bitsys.odoo.com",

    'sequence': 1,

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/vertical_patient_views.xml',
        'views/vertical_treatment_view.xml',
       
        'data/sequences.xml',

        'reports/report_action.xml',
        'reports/vertical_patient_report.xml',      
    ],


    'summary': """
        Test de Desarrollador""",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    
    # "active": True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
