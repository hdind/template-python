import enum

class IBGE(str):
    URL_BASE: str = 'https://servicodados.ibge.gov.br/api/v1/'
    COUNTRY: str = 'paises'
    KPI: str = 'indicadores'
    PERIOD: str = 'periodo'