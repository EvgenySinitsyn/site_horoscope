from datetime import datetime



class FoundDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

class MyFloatConverter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

class MyDateConverter:
    regex = '^(((0[1-9]|[12][0-9]|30)[-/]?(0[13-9]|1[012])|31[-/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[-/]?02)[-/]?[0-9]{4}|29[-/]?02[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')