import pandas as pd
import glob
import os
import re
import numpy as np
import datetime as dt
import math
from function import parser

directory = r'C:\Users\Alina\Desktop\Работа\Попластовый план\Протоколы ПТД'
if os.path.exists(directory + r'\all.xlsx'):
    os.remove(directory + r'\all.xlsx')

# названия столбцов
name_columns = pd.MultiIndex.from_tuples(
    [('Месторождение', ''), ('Объект', ''), ('Район', ''), ('Залежь', ''), ('Средняя глубина залегания кровли', 'м'), ('Абсолютная отметка ВНК', 'м'), ('Абсолютная отметка ГНК', 'м'),
     ('Абсолютная отметка ГВК', 'м'), ('Тип залежи', ''), ('Тип коллектора', ''), ('Площадь нефтегазоносности', 'тыс.м2'), ('Средняя общая толщина', 'м'), ('Средняя эффективная нефтенасыщенная толщина', 'м'),
     ('Средняя эффективная газонасыщенная толщина', 'м'), ('Средняя эффективная водонасыщенная толщина', 'м'), ('Коэффициент пористости', 'доли ед.'), ('Коэффициент нефтенасыщенности ЧНЗ', 'доли ед.'),
     ('Коэффициент нефтенасыщенности ВНЗ', 'доли ед.'), ('Коэффициент нефтенасыщенности пласта', 'доли ед.'), ('Коэффициент газонасыщенности пласта', 'доли ед.'),
     ('Проницаемость', 'мкм2'), ('Коэффициент песчанистости', 'доли ед.'), ('Расчлененность', 'ед.'), ('Начальная пластовая температура', ' оС'), ('Начальное пластовое давление', 'МПа'),
     ('Вязкость нефти в пластовых условиях', 'мПа*с'), ('Плотность нефти в пластовых условиях', 'г/см3'), ('Плотность нефти в поверхностных условиях', 'г/см3'),
     ('Объемный коэффициент нефти', 'доли ед.'), ('Содержание серы в нефти', '%'), ('Содержание парафина в нефти', '%'), ('Давление насыщения нефти газом', 'МПа'),
     ('Газосодержание', 'м3/т'), ('Давление начала конденсации', 'МПа'), ('Плотность конденсата в стандартных условиях', 'г/см3'), ('Вязкость конденсата в стандартных условиях', 'мПа*с'),
     ('Потенциальное содержание стабильного конденсата в газе (С5+)', 'г/м3'), ('Содержание сероводорода', '%'), ('Вязкость газа в пластовых условиях', 'мПа*с'),
     ('Плотность газа в пластовых условиях', 'г/см3'), ('Коэффициент сверхсжимаемости газа', 'доли ед.'), ('Вязкость воды в пластовых условиях', 'мПа*с'),
     ('Плотность воды в поверхностных условиях', 'г/см3'), ('Сжимаемость', ''), ('нефти', '1/МПа×10-4 '), ('воды', '1/МПа×10-4 '), ('породы', '1/МПа×10-4 '),
     ('Коэффициент вытеснения (водой)', 'доли ед.'), ('Коэффициент вытеснения (газом)', 'доли ед.'), ('Коэффициент продуктивности', 'м3/сут * МПа'),
     ('Коэффициенты фильтрационных сопротивлений:', ''), ('А', 'МПа2/(тыс.м3/сут)'), ('В', 'МПа2/(тыс.м3/сут)')])


df = parser(directory)

# df.columns = name_columns

df.to_excel(directory + r'\all.xlsx', index=False)