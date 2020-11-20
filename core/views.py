from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """ Retorna 12 labels(meses) para representação do 'x' """
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return labels

    def get_providers(self):
        """ Retorna os nomes dos datasets """
        datasets = [
            "Heineken",
            "Eisenbahn",
            "Corona",
            "Brahma",
            "Skol",
            "Bohemia"
        ]
        return datasets

    def get_data(self):
        """
         retorna 6 datasets para plotar o grafico
         cada linha representará um dataset
         cada coluna representará um label

         a quantidade de dados precisa ser igual aos datasets / labels

         *12 labels = 12 colunas
         6 datasets = 6 linhas*
        """
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 100),  # jan
                    randint(1, 100),  # feb
                    randint(1, 100),  # mar
                    randint(1, 100),  # apr
                    randint(1, 100),  # may
                    randint(1, 100),  # jun
                    randint(1, 100),  # jul
                    randint(1, 100),  # aug
                    randint(1, 100),  # sep
                    randint(1, 100),  # oct
                    randint(1, 100),  # nov
                    randint(1, 100)  # dec
                ]
            dados.append(dado)
        return dados
