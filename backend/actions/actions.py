from rasa_sdk import Action
from rasa_sdk.events import SlotSet


def obter_texto_emocional(emocao):

    if emocao == "frustracao":
        return (
            "Entendo que isso possa estar sendo difícil. "
            "Vamos analisar o conceito passo a passo."
        )

    elif emocao == "confusao":
        return (
            "Vamos simplificar a ideia."
        )

    elif emocao == "ansiedade":
        return (
            "Sem pressa. O importante é compreender um conceito de cada vez."
        )

    elif emocao == "motivacao":
        return (
            "Excelente! Vamos avançar um pouco mais."
        )

    elif emocao == "prazer":
        return (
            "Que bom que você está gostando do aprendizado!"
        )

    elif emocao == "desafio":
        return (
            "Excelente! Vamos explorar alguns detalhes extras."
        )

    elif emocao == "tedio":
        return (
            "Vamos usar um exemplo prático para tornar isso mais interessante."
        )

    return ""
    
class ActionSalvarFrustracao(Action):

    def name(self):
        return "action_salvar_frustracao"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Entendo sua frustração. Vamos resolver isso juntos."
        )

        return [SlotSet("emocao", "frustracao")]


class ActionSalvarConfusao(Action):

    def name(self):
        return "action_salvar_confusao"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Tudo bem ficar confuso às vezes. Vamos identificar exatamente onde está a dúvida."
        )

        return [SlotSet("emocao", "confusao")]


class ActionSalvarAnsiedade(Action):

    def name(self):
        return "action_salvar_ansiedade"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Sem pressa. Vamos resolver um passo de cada vez."
        )

        return [SlotSet("emocao", "ansiedade")]


class ActionSalvarMotivacao(Action):

    def name(self):
        return "action_salvar_motivacao"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Que ótimo! Sua motivação é um grande aliado no aprendizado."
        )

        return [SlotSet("emocao", "motivacao")]


class ActionSalvarPrazer(Action):

    def name(self):
        return "action_salvar_prazer"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Fico feliz que você esteja gostando da atividade!"
        )

        return [SlotSet("emocao", "prazer")]


class ActionSalvarDesafio(Action):

    def name(self):
        return "action_salvar_desafio"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Excelente! Encarar desafios é uma ótima forma de aprender."
        )

        return [SlotSet("emocao", "desafio")]


class ActionSalvarTedio(Action):

    def name(self):
        return "action_salvar_tedio"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(
            text="Talvez possamos encontrar uma forma mais interessante de abordar esse conteúdo."
        )

        return [SlotSet("emocao", "tedio")]
    

class ActionExplicarRepeticao(Action):

    def name(self):
        return "action_explicar_repeticao"

    def run(self, dispatcher, tracker, domain):

        emocao = tracker.get_slot("emocao")
        texto_emocional = obter_texto_emocional(emocao)

        explicacao = (
            "\n\nEstruturas de repetição permitem executar um bloco de código várias vezes."
        )

        exemplo = (
            "\n\nExemplo em Java:\n"
            "for(int i = 0; i < 5; i++) {\n"
            "    System.out.println(i);\n"
            "}"
        )

        observacao = (
            "\n\nNesse exemplo, o laço for executa o bloco de código 5 vezes, "
            "exibindo os números de 0 a 4."
        )

        mensagem = texto_emocional + explicacao + exemplo + observacao

        dispatcher.utter_message(text=mensagem)

        return [SlotSet("assunto", "repeticao")]
    


class ActionExplicarVariavel(Action):

    def name(self):
        return "action_explicar_variavel"

    def run(self, dispatcher, tracker, domain):

        emocao = tracker.get_slot("emocao")
        texto_emocional = obter_texto_emocional(emocao)

        # Explicação do conceito
        explicacao = (
            "\n\nUma variável é um espaço utilizado para armazenar informações "
            "durante a execução de um programa."
        )

        # Exemplo em Java
        exemplo = (
            "\n\nExemplo em Java:\n"
            "String nome = \"Maria\";\n"
            "int idade = 17;"
        )

        # Observação do exemplo
        observacao = (
            "\n\nNesse exemplo, a variável 'nome' armazena um texto "
            "e a variável 'idade' armazena um número inteiro."
        )

        mensagem = texto_emocional + explicacao + exemplo + observacao

        dispatcher.utter_message(text=mensagem)

        return [SlotSet("assunto", "variavel")]
    
class ActionExplicarCondicional(Action):

    def name(self):
        return "action_explicar_condicional"

    def run(self, dispatcher, tracker, domain):

        emocao = tracker.get_slot("emocao")
        texto_emocional = obter_texto_emocional(emocao)

        # Explicação do conceito
        explicacao = (
            "\n\nUma estrutura condicional permite que o programa tome decisões "
            "com base em condições."
        )

        # Exemplo em Java
        exemplo = (
            "\n\nExemplo em Java:\n"
            "int idade = 18;\n\n"
            "if (idade >= 18) {\n"
            "    System.out.println(\"Maior de idade\");\n"
            "} else {\n"
            "    System.out.println(\"Menor de idade\");\n"
            "}"
        )

        # Observação do exemplo
        observacao = (
            "\n\nNesse exemplo, o programa verifica se a idade é maior ou igual a 18. "
            "Se a condição for verdadeira, exibe 'Maior de idade'. "
            "Caso contrário, exibe 'Menor de idade'."
        )

        mensagem = texto_emocional + explicacao + exemplo + observacao

        dispatcher.utter_message(text=mensagem)

        return [SlotSet("assunto", "condicional")]
    
    
class ActionExplicarFuncao(Action):

    def name(self):
        return "action_explicar_funcao"
    



    def run(self, dispatcher, tracker, domain):

        emocao = tracker.get_slot("emocao")
        texto_emocional = obter_texto_emocional(emocao)

        explicacao = (
            "\n\nEm Java, métodos são blocos de código reutilizáveis que executam tarefas específicas."
        )

        exemplo = (
            "\n\nExemplo em Java:\n"
            "public static void saudacao() {\n"
            "    System.out.println(\"Olá!\");\n"
            "}"
        )

        observacao = (
            "\n\nNesse exemplo, o método 'saudacao' pode ser chamado sempre que quisermos exibir a mensagem 'Olá!'."
        )

        mensagem = texto_emocional + explicacao + exemplo + observacao

        dispatcher.utter_message(text=mensagem)

        return [SlotSet("assunto", "funcao")]
    
    
    
    
class ActionExercicio(Action):

    def name(self):
        return "action_exercicio"

    def run(self, dispatcher, tracker, domain):

        emocao = tracker.get_slot("emocao")
        assunto = tracker.get_slot("assunto")

        if assunto == "variavel":

            if emocao == "frustracao":
                mensagem = (
                    "Vamos começar com algo simples.\n\n"
                    "Crie uma variável chamada nome e armazene seu nome nela."
                )

            elif emocao == "desafio":
                mensagem = (
                    "Desafio:\n\n"
                    "Crie um cadastro contendo nome, idade e altura utilizando variáveis de tipos diferentes."
                )

            else:
                mensagem = (
                    "Exercício:\n\n"
                    "Crie variáveis para armazenar nome, idade e cidade."
                )

        elif assunto == "funcao":

            if emocao == "frustracao":
                mensagem = (
                    "Vamos praticar devagar.\n\n"
                    "Crie um método chamado saudacao que exiba a mensagem 'Olá'."
                )

            elif emocao == "desafio":
                mensagem = (
                    "Desafio:\n\n"
                    "Crie um método que receba três notas e retorne a média delas."
                )

            else:
                mensagem = (
                    "Exercício:\n\n"
                    "Crie um método chamado calcularSoma que receba dois números."
                )

        elif assunto == "repeticao":

            if emocao == "frustracao":
                mensagem = (
                    "Vamos começar com algo simples.\n\n"
                    "Utilize um laço for para exibir os números de 1 a 5."
                )

            elif emocao == "desafio":
                mensagem = (
                    "Desafio:\n\n"
                    "Utilize um laço for para exibir apenas os números pares de 1 a 100."
                )

            else:
                mensagem = (
                    "Exercício:\n\n"
                    "Utilize um laço for para exibir os números de 1 a 10."
                )

        elif assunto == "condicional":

            if emocao == "frustracao":
                mensagem = (
                    "Vamos praticar com um exemplo simples.\n\n"
                    "Crie um if que verifique se uma pessoa é maior de idade."
                )

            elif emocao == "desafio":
                mensagem = (
                    "Desafio:\n\n"
                    "Crie uma estrutura que classifique uma nota como A, B, C ou D."
                )

            else:
                mensagem = (
                    "Exercício:\n\n"
                    "Crie um programa que informe se um número é positivo ou negativo."
                )

        else:
            mensagem = (
                "Primeiro escolha um conteúdo para estudar, como variáveis, funções, condicionais ou repetições."
            )

        dispatcher.utter_message(text=mensagem)

        return []