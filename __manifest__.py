{
    'name': 'OpenWeatherMAp Integration',
    'version': '1.0',
    'summary': 'Integración con la API de OpenWeatherMap',
    'description': 'Obtención de datos meteorológicos en tiempo real',
    'author': 'Marta Enríquez Figueroa',
    'category': 'Tools',
    'depends': ['base'],
    'icon':'/openweathermap_odoo/static/description/icon57.png',
    'data': [
        'security/ir.model.access.csv',
        'views/weather_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}