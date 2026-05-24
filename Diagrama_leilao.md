
### Diagrama de classe para um aplicativo de leilão

@startuml ModeloApp

class Pessoa {
 -nome: Char
 -sobrenome: Char
 -email: Email
 -data_cadastro: Date
 +toString()
}

class Usuario {
 -ativo: Boolean
 -pontuacao: Integer
 -cpf: Char
 -perfil: CharChoices
 +toString()
}

class Endereco {
 -cep: Char
 -numero: Integer
 -complemento: Char
 -principal: Boolean
 -usuario: ForeignKey[Usuario]
 +toString()
}

class Categoria {
 -nome: Char
 -descricao: Text
 -codigo_setor: Integer
 -destaque: Boolean
 +toString()
}

class Produto {
 -titulo: Char
 -detalhes: Text
 -condicao_novo: Boolean
 -peso_kg: Float
 -categoria: ForeignKey[Categoria]
 -dono: ForeignKey[Usuario]
 +toString()
}

class Leilao {
 -lance_inicial: Decimal
 -data_encerramento: DateTime
 -ativo: Boolean
 -status: CharChoices
 -produto: OneToOne[Produto]
 +toString()
}

class Lance {
 -valor: Decimal
 -data_lance: DateTime
 -valido: Boolean
 -ip_origem: Char
 -leilao: ForeignKey[Leilao]
 -comprador: ForeignKey[Usuario]
 +toString()
}

class Pagamento {
 -metodo: CharChoices
 -valor_total: Float
 -pago: Boolean
 -data_pagamento: DateTime
 -leilao: OneToOne[Leilao]
 +toString()
}

class Envio {
 -transportadora: Char
 -codigo_rastreio: Char
 -data_postagem: Date
 -entregue: Boolean
 -pagamento: OneToOne[Pagamento]
 +toString()
}

class Avaliacao {
 -nota: Integer
 -comentario: Text
 -data_avaliacao: Date
 -visivel: Boolean
 -avaliador: ForeignKey[Usuario]
 -avaliado: ForeignKey[Usuario]
 -leilao: ForeignKey[Leilao]
 +toString()
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
Leilao *--> Avaliacao : 1..1

@enduml