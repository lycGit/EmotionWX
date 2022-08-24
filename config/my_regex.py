from werkzeug.routing import BaseConverter


class MobileConverter(BaseConverter):
    regex = '^1[3-9]\d{9}'