# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_da_compra = '2022-12-20'
data_str_formatada = '%d/%m/%Y %H:%M:%S'

data_da_compra_final = '2025-04-20'
valor_total = 100000000
valor_parcela = 27777.78
valor_pago_atual = 0

data_da_compra_final_dt = datetime.strptime(data_da_compra_final, "%Y-%m-%d")
contador = 0

while contador <= 35:
    contador += 1
    
    data_da_compra_dt = datetime.strptime(data_da_compra, "%Y-%m-%d")

    data_da_compra_dt += relativedelta(months=1)

    data_da_compra_formatada = data_da_compra_dt.strftime(data_str_formatada)
    
    valor_que_falta_pagar = valor_total - valor_pago_atual
    valor_pago_atual += valor_parcela
    print(
        f"=======================================\nData de Vencimento: {data_da_compra_dt}\nValor Pago: {valor_pago_atual}\nValor que ainda falta pagar: {valor_que_falta_pagar}\nValor da Parcela: {valor_parcela}"
        )

    data_da_compra = data_da_compra_dt.strftime('%Y-%m-%d')

    
    
