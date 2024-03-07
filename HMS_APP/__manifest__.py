{
    'name': 'Hospital Management System',
    'version': '17.0.0.1.0',
    'summary': 'Hospital Management System Module',
    'author': 'Mostafa Hefzy',
    'category': 'Healthcare',
    'depends': ['base'],

    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
    ],
    'application': True,
}