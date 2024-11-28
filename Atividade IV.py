menu = {
    "1": ("Pizza", 25.00),
    "2": ("Hambúrguer", 20.00),
    "3": ("Macarrão com Carne", 30.00),
    "4": ("Dogão Duplo", 15.00),
    "5": ("Macarrão com Frango", 28.00),
    "6": ("Espetinho", 22.00),
    "7": ("Lasanha", 24.00)
}

pedidos = []
total = 0

# Exibe o menu inicial
print("Bem-vindo ao nosso restaurante!")
print("Menu:")
for codigo, (nome, preco) in menu.items():
    print(f"{codigo}: {nome} - R${preco:.2f}")

# Loop para realizar os pedidos
while True:
    codigo_pedido = input("Escolha o código do prato ou '0' para finalizar: ")
    
    if codigo_pedido == "0":
        break
    elif codigo_pedido in menu:
        nome, preco = menu[codigo_pedido]
        pedidos.append((nome, preco))
        total += preco
    else:
        print("Código inválido!")

    if input("Deseja adicionar outro prato? (s/n): ").strip().lower() != 's':
        break

# Escolhe a forma de pagamento
forma_pagamento = input("Forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
if forma_pagamento == "1":
    desconto = total * 0.10
    valor_final = total - desconto
    ajuste = -desconto
    forma_pagamento_nome = "À vista"
elif forma_pagamento == "2":
    acrescimo = total * 0.10
    valor_final = total + acrescimo
    ajuste = acrescimo
    forma_pagamento_nome = "Cartão de crédito"
else:
    forma_pagamento_nome = "Indefinida"
    valor_final = total
    ajuste = 0

# Exibe o resumo do pedido
print("\n--- Resumo do Pedido ---")
for nome, preco in pedidos:
    print(f"- {nome}: R${preco:.2f}")
print(f"Subtotal: R${total:.2f}")
print(f"Forma de pagamento: {forma_pagamento_nome}")
if ajuste != 0:
    print(f"Ajuste: R${ajuste:.2f}")
print(f"Valor final a ser pago: R${valor_final:.2f}")