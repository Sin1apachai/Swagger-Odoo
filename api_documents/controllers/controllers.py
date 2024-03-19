from odoo import http
from odoo.http import request
import os

class SwaggerController(http.Controller):
    @http.route('/api/docs', auth='public')
    def index(self, **kw):
        return http.request.render('api_documents.swagger_ui_template', {})

    # @http.route('/api_documents/swagger.yaml', auth='public')
    # def spec(self, **kw):
    #     spec_path = os.path.join(os.path.dirname(__file__), 'static', 'swagger.yaml')
    #     with open(spec_path, 'r') as f:
    #         spec = f.read()
    #     return request.make_response(spec, headers=[('Content-Type', 'text/plain')])
