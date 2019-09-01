'''Initialize application and import all app component

Author: Ukor Jidechi
Orgainization: TedX Ebonyi State Nigeria
Maintainers: []
'''

from flask import Flask

app = Flask(__name__)

from tedxEbonyiState import routes

