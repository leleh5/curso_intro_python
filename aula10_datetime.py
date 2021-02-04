from datetime import date, time, datetime, timedelta

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)

def trabalhando_datetime():
    data_hora_atual = datetime.now()
    data_atual = data_hora_atual.strftime('%d/%m/%Y')
    hora_atual = data_hora_atual.strftime('%H:%M:%S')
    print('Data de hoje: {date}. Hora: {time}'.format(date=data_atual, time=hora_atual))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_hora_atual.weekday()])
    data_string = '01/09/2022 20:20:20'
    data_convert = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convert)

def trabalhando_timedelta():
    data_atual = datetime.now()
    nova_data = data_atual - timedelta(days= 366, hours= 2, minutes= 15)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_date()
    #trabalhando_time()
    #trabalhando_datetime()
    trabalhando_timedelta()