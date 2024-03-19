# -*- coding: utf-8 -*-
{
    'name': "API Documents",

    'summary': """
        API Documents Interface""",

    'description': """
        API Documents Interface by Swagger UI
    """,

    'author': "blueminktech",
    'website': "https://www.bluemink.tech/",

    'category': 'base',
    'version': '1.0',

    'depends': ['base','web', 'base_api', 'openapi'],

    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'my_module/static/lib/swagger-ui/dist/**/*',
            'my_module/static/src/js/swagger.js',
        ],
    },
}
