# импорт функций

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):return x.value
#загрузить книгу excel
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
#значения лет из колонки А
years = list(map(getvalue, sheet['A'][1:]))
#значения температур из колонки C
temp = list(map(getvalue, sheet['C'][1:]))
#значения активности из колонки D
activity = list(map(getvalue, sheet['D'][1:]))
#график температура/года
pyplot.plot(years, temp, label="Относит. температура")
#график активность/года
pyplot.plot(years, activity, label="Активность солнца")
#обозначаем оси
pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность солнца')
#легенда
pyplot.legend(loc='upper left')
#выводим на экран
pyplot.show()
