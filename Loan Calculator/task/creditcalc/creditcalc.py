import argparse
import math


def annuity_payment(l_principal, number_payments, annual_interest_rate):
    # l_principal основная сумма кредита
    number_payments = number_payments  # количество платежей, в течении которых будут производить выплаты
    nominal_rate = float(annual_interest_rate / (12 * 100))  # расчет номинальной процентной ставки
    a_payment = (l_principal * float(nominal_rate) * math.pow(1 + float(nominal_rate), number_payments)) / (math.pow(1 + float(nominal_rate), number_payments) - 1)  # расчет аннуитетного платежа
    print(f"Your annuity payment = {math.ceil(a_payment)}!")
    print()
    print(f"Overpayment = {int(math.ceil(a_payment) * number_payments - l_principal)}")  # значение аннуит-го платежа


def diff_payment(l_principal, numbers_payments, interest_rate):
    # l_principal основная сумма кредита
    # numbers_payments количество платежей, в течении которых будут производить выплаты
    nominal_rate = interest_rate / (12 * 100)  # расчет номинальной процентной ставки
    # расчет дифференциального платежа
    x = list()

    for i in list(range(numbers_payments)):
        i += 1
        diff_payment_month = (l_principal / numbers_payments) + nominal_rate * (l_principal - (l_principal * (i - 1) / numbers_payments))
        print(f"Month {i}: =", math.ceil(diff_payment_month))
        x.append(math.ceil(diff_payment_month))
    print()
    print("Overpayment =",  sum(x) - math.ceil(l_principal))


def loan_principal(a_payment, numbers_payments, interest_rate):
    # a_payment планируемая сумма ежемесячного платежа
    # numbers_payments количество платежей, в течении которых будут производить выплаты
    # interest_rate планируемая процентная ставка
    nominal_rate = interest_rate / (12 * 100)
    l_principal = a_payment / (nominal_rate * math.pow((1 + nominal_rate), numbers_payments) / (math.pow(1 + nominal_rate, numbers_payments) - 1))
    print(f"Your loan principal = {math.floor(l_principal)}!")
    print("Overpayment =", math.floor(a_payment * numbers_payments - math.floor(l_principal)))


# loan_principal(8722, 120, 5.6)


def time_credit(l_principal, monthly_payment, interest_rate):
    # l_principal основная сумма кредита
    # monthly_payment ежемесячный платеж:
    # interest_rate планируемая процентная ставка
    nominal_rate = float(interest_rate / (12 * 100))
    time = round(math.log(float(monthly_payment) / (float(monthly_payment) - nominal_rate * float(l_principal)), nominal_rate + 1))
    if time == 1:
        print(f"It will take {math.ceil(time)} month to repay this loan!")
    if 1 < time < 12:
        print(f"It will take {math.ceil(time)} months to repay this loan!")
    if time > 12:
        print(f"It will take {math.floor(time / 12)} years to repay this loan!")
    print(f"Overpayment = {math.floor(monthly_payment * time - l_principal)}")


parser = argparse.ArgumentParser(
    prog="Кредитный калькулятор",
    description="Проект Кредитный калькулятор (Hyperskill)")

parser.add_argument('--type', type=str, choices=("annuity", "diff"), help="выбор типа оплаты")
parser.add_argument('--principal', type=float, help="расчет обоих типов платежей")
parser.add_argument('--periods', type=int, help="количество месяцев")
parser.add_argument('--payment', type=float, help="сумма ежемесячного платежа")
parser.add_argument('--interest', type=float, help="интересная процентная ставка")


args = parser.parse_args()
parameters = [args.type, args.principal, args.periods, args.payment, args.interest]



if args.type == 'diff' and abs(args.principal) > 0 and args.periods and args.interest:
    diff_payment(args.principal, args.periods, args.interest)

elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    annuity_payment(args.principal, args.periods, args.interest)

elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    loan_principal(args.payment, args.periods, args.interest)

elif args.type == 'annuity' and args.principal and args.payment and args.interest:
    time_credit(args.principal, args.payment, args.interest)

elif args.type != ('annuity' or 'diff') or args.principal != float or args.periods != int or args.payment != float or args.interest != int:
    print("Incorrect parameters.")

