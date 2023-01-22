# Проверка датасета на наличие пропусков в данных.
df_origal = data.copy()
df_origal = df_origal.drop_duplicates(ignore_index=True)
df_isnull = df_origal.isnull()

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

del_list_int = []
del_list_str = []

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
