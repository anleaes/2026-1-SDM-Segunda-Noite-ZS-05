
### Diagrama de classe para um aplicativo de leilão

- Validar lógica de leilão automatico
- Validar relação comparativa entre Order --- Orderitem --- Product

@startuml ModeloApp

class Pessoa{
 -nome: Char
 -sobrenome: Char
 -email: Email
 -data_cadastro: Date
 +toString()
}

class Usuario{
 -ativo: Boolean
 -pontuacao: Integer
 -cpf: Char
 -perfil: CharChoices
 -leiloes_automaticos: ManyToMany[Leilao]
 +toString()
}

class Endereco{
 -cep: Char
 -numero: Integer
 -complemento: Char
 -principal: Boolean
 -usuario: ForeignKey[Usuario]
 +toString()
}

class Categoria{
 -nome: Char
 -descricao: Text
 -codigo_setor: Integer
 -destaque: Boolean
 +toString()
}

class Produto{
 -titulo: Char
 -detalhes: Text
 -condicao_novo: Boolean
 -peso_kg: Float
 -categoria: ForeignKey[Categoria]
 -dono: ForeignKey[Usuario]
 +toString()
}

class Leilao{
 -lance_inicial: Decimal
 -data_encerramento: DateTime
 -ativo: Boolean
 -produto: OneToOne[Produto]
 +toString()
}

class Lance{
 -valor: Decimal
 -data_lance: DateTime
 -valido: Boolean
 -leilao: ForeignKey[Leilao]
 -comprador: ForeignKey[Usuario]
 +toString()
}

class Pagamento{
 -metodo: CharChoices
 -valor_total: Float
 -pago: Boolean
 -lance: OneToOne[Lance]
 +toString()
}

class Envio{
 -transportadora: Char
 -codigo_rastreio: Char
 -data_postagem: Date
 -entregue: Boolean
 -pagamento: OneToOne[Pagamento]
 +toString()
}

class Avaliacao{
 -nota: Integer
 -comentario: Text
 -data_avaliacao: Date
 -visivel: Boolean
 -avaliador: ForeignKey[Usuario]
 -avaliado: ForeignKey[Usuario]
 -lance: ForeignKey[Lance]
 +toString()
}

class LanceAutomatico{
 -limite_maximo: Decimal
 -ativo: Boolean
 -data_configuracao: Datetime
 -usuario: ForeignKey[Usuario]
 -leilao: ForeignKey[Leilao]
}

Usuario -up-|> Pessoa: 1..1
Usuario *--> Endereco : 1..n
Categoria *--> Produto : 1..n
Usuario *--> Produto : 1..n
Produto *--> Leilao : 1..1
Leilao *--> Lance : 0..n
Usuario *--> Lance : 0..n
Leilao *--> Pagamento : 1..1
Pagamento *--> Envio : 1..1
Usuario *--> Avaliacao : 0..n
Avaliacao *--> Lance : 1..1
Usuario *--> LanceAutomatico : 0..n
Lance *--> LanceAutomatico : 0..n

@enduml