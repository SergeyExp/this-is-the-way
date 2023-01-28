# Проверка датасета на наличие пропусков в данных.
import pandas as pd
import numpy as np

# Выбор датасета и удаление дубликатов строк
name = input("Введите датасет: ")
data = pd.read_csv(f'F:\\data\\{name}.csv')
df_origal = data.copy()
df_origal = df_origal.drop_duplicates(ignore_index=True)
df_isnull = df_origal.isnull()

# функция замены пустых данных на 'unknown' для текстовых признаков
def get_col_str(col, df_origal, df_isnull): 
    countt = 0
    for i in range(len(df_isnull)):
        if df_isnull.loc[i, col] == True:
            df_origal.loc[i, col] = 'unknown'
            countt += 1
    procent = round(countt * 100 / len(df_isnull), 2)
    if countt != 0:
        print(f'в {col}, пропусков {countt}, это {procent} % пропущеных значений')
    else:
        print(f'в {col}, пропусков значений нет')
    if procent > 30:
        del_list_str.append(col)
        print(f'{col} записан в лист на удаление, пропусков более 30%')
    return

# функция замены пустых данных на -1 для числовых признаков
def get_col_int(col, df_origal, df_isnull):
    countt = 0
    for i in range(len(df_isnull)):
        if df_isnull.loc[i, col] == True:
            df_origal.loc[i, col] = -1
            countt += 1
    procent = round(countt * 100 / len(df_isnull), 2)
    if countt != 0:
        print(f'в {col}, пропусков {countt}, это {procent} % пропущеных значений')
    else:
        print(f'в {col}, пропусков значений нет')
    if procent > 30:
        del_list_int.append(col)
        print(f'{col} записан в лист на удаление, пропусков более 30%')
    return

# списки для удаления признаков с пропусками 30%+
del_list_int = []
del_list_str = []

# разделение по признаку(числовой\текстовый) и его преобразование
for col in df_origal.columns:
    if df_origal[col].dtype == np.int64 or df_origal[col].dtype == np.float64:
        print('-------------------------------')
        print(f'начат процесс преобразования в столбце {col}')
        get_col_int(col, df_origal, df_isnull)
        print('процесс завершен')
    else:
        print('-------------------------------')
        print(f'начат процесс преобразования в столбце {col}')
        get_col_str(col, df_origal, df_isnull)
        print('процесс завершен')

# выбор и удаление признаков из списка del_list_int и del_list_str
del_info = input(f"Удалить признаки {del_list_int} \n и {del_list_str}?")
if del_info == 'y':
    for col in del_list_int:
        df_origal = df_origal.drop(col, axis=1)
    for col in del_list_str:
        df_origal = df_origal.drop(col, axis=1)
else:
    pass
df_origal.to_csv(f'F:\\data\\{name}_clean.csv')
print(f'записан файл {name}_clean')