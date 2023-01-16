import datetime as dt

class Calculator:
    """Patent class is used to to implement standart calculator funtions."""
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        return sum(record.amount for record in self.records
                if record.date == today)

    def get_week_stats(self):
        today = dt.date.today()
        date_week_ago = today - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                if date_week_ago < record.date <= today)

    def get_remained(self):
        remained = self.limit - self.get_today_stats()
        return remained


class Record:
    """Record used for storing records."""
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()

        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def __str__(self):
        return f'Record({self.amount}, {self.date}, {self.comment})'


class CashCalculator(Calculator):
    """Cash calculator calculates and monitors money."""
    USD_RATE = 68.32
    EURO_RATE = 74.00
    RUB_RATE = 1.00

    def get_today_cash_remained(self, currency):
        remained = self.get_remained()
        currency_dir = {
            'eur': ('Euro', self.EURO_RATE,),
            'usd': ('USD', self.USD_RATE,),
            'rub': ('руб', self.RUB_RATE,)
        }
        currency_name, currency_rate = currency_dir[currency]
        debt_1 = remained / currency_rate
        debt_2 = abs(round(debt_1, 2))
        if remained == 0:
            return 'Денег нет, держись'
        if currency not in currency_dir:
            raise ValueError('валюта неверная, правильные: Usd, Eur, Руб.')
        if remained < 0:
            return(
                'Денег нет, держись: твой долг '
                f'- {debt_2} {currency_name}'
            )
        return ('На сегодня осталось '
                f'{debt_2} {currency_name}')


class CaloriesCalculator(Calculator):
    """CaloriesCalculator calculates and monitors calories."""
    def get_calories_remained(self):
        g_rem = self.get_remained()
        if g_rem <= 0:
            return 'Хватит есть!'
        return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                f'калорийностью не более {g_rem} кКал')