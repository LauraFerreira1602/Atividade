class Compra:
    def __init__(self, codigo, nome_produto, preco, tipo, quantidade_produtos):
        self.codigo = codigo
        self.nome_produto = nome_produto
        self.preco = preco
        self.tipo = tipo
        self.quantidade_produtos = quantidade_produtos


    def apresentar(self):
        print(f'Codigo da compra: {self.codigo}\n'
              f'Nome do produto: {self.nome_produto}\n'
              f'Tipo do produto: {self.tipo}\n'
              f'O valor do produto é: {self.preco}\n'
              f'Quantidade de produto: {self.quantidade_produtos}\n'
              )


    def valor_compra(self):
        valor_total = self.preco * self.quantidade_produtos
        print(f'O valor da compra é: {valor_total}') #parecido idade Bruna


        print("-" * 20)


C1 = Compra("298365", "Tenis", 155.90, "Calçado", 1)
C1.apresentar()
C1.valor_compra()


class Pedido(Compra):
    def __init__(self, codigo, nome_produto, preco, tipo, quantidade_produtos):
        super().__init__( codigo, nome_produto, preco, tipo, quantidade_produtos=0)
        self.realizacao = True
        self.proximidade = False
        self.entrega = False

    def apresentar(self):
        print(f'Codigo do pedido: {self.codigo}\n'
            f'Nome do produto: {self.nome_produto}\n'
            f'Preço: {self.preco}\n'
            f'Tipo do produto: {self.tipo}\n'
            f'Quantidade de produto: {self.quantidade_produtos}\n'
            )

        if self.realizacao:
            print("O pedido foi realizado com sucesso!")

        else:
            print("O pedido não pode ser realizado.")


        if self.proximidade:
            print("Seu pedido esta proximo de ser entregue.")

        else:
            print("Seu pedido esta distante.")


        if self.entrega:
            print("Seu pedido foi entregue com sucesso! ")

        else:
            print("Seu pedido sera entregue em breve.")

    def realizar(self):
        if self.realizacao:
           print(f'O pedido foi realizado com sucesso!')

        else:
            self.realizacao = False
            print(f'Ouve algum problema,o pedido não pode ser realizado.')


    def distancia(self):
        self.proximidade = True

    def proximidade(self):
       if print(f'Seu pedido esta proximo de ser entregue.')


        else:
            self.proximidade:
            print(f'Seu pedido ainda esta distante.')



    def correrios_entregar(self):
        self.entrega = True


    def entrega(self):
        if print(f'O pedido foi entregue com sucesso!')

        else:
            self.entrega:
            print(f'Seu pedido sera entregue em breve.')




P1 = Pedido("298365", "Tenis", 155.90, "Calçado", 1)
