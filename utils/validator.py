import re

def validate_cnpj(cnpj):
    """Valida formato CNPJ"""
    pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    return re.match(pattern, cnpj) is not None