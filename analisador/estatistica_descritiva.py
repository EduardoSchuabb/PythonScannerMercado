import pandas as pd

def calculoMediaTodosFIIs(data_frame_codigo):
    # Proceedimento para calculo da média de um código FIIs
    # seguindo padrao de salvamento dos arquivos .csv relacionados as FIIs.
    
    serie_MM5 = pd.Series()
    serie_MM10 = pd.Series()
    serie_MM15 = pd.Series()

    # média móvel de 5 dias
    serie_MM5 = data_frame_codigo['close'].rolling(window=5).mean()
    serie_MM5 = serie_MM5.fillna(0).round(2)

    # média móvel de 10 dias
    serie_MM10 = data_frame_codigo['close'].rolling(window=10).mean()
    serie_MM10 = serie_MM10.fillna(0).round(2)

    # média móvel de 15 dias
    serie_MM15 = data_frame_codigo['close'].rolling(window=15).mean()
    serie_MM15 = serie_MM15.fillna(0).round(2)

    data_frame_estatistico = pd.DataFrame({
        'date': data_frame_codigo['date'],
        'MM5': serie_MM5,
        'MM10': serie_MM10,
        'MM15': serie_MM15
    })

    return data_frame_estatistico