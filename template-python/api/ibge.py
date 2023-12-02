import requests
from utils.config import IBGE


class IBGEAPI:
    """
        This class was built to access IBGE API.
    """    
    def __init__(self):
        self.base_url = IBGE.URL_BASE

    def get_kpi(self, countries, periods):
        url = f"{self.base_url}{IBGE.COUNTRY}/{countries}/{IBGE.KPI}?{IBGE.PERIOD}={periods}"
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Erro na Solicitação!!! Código de Status: {response.status_code}")
                return None
        except Exception as e:
            print(f"Erro ao Acessar a API: {str:(e)}")
            

if __name__ == "__main__":
    ibge = IBGEAPI()
    countries = "AR|BR|US"
    periods = "2016"
    dados = ibge.get_kpi(countries, periods)
    
    if dados:
        print(dados)
