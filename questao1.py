
def calcular_cashback(valor_compra: float, desconto_percentual: float, vip: bool) -> float:

    valor_final = valor_compra * (1 - desconto_percentual / 100)

    #Cashback base
    cashback_base = valor_final * 0.05

    #promoção de compras acima de 500 com dobro de cashback
    if valor_final > 500:
        cashback_base *= 2

    # Bônus VIP 
    bonus_vip = cashback_base * 0.10 if vip else 0.0

    cashback_total = cashback_base + bonus_vip

    return round(cashback_total, 2)

