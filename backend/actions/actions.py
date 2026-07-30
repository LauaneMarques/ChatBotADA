from rasa_sdk import Action
from rasa_sdk.events import SlotSet


def obter_texto_emocional(emocao):
    if emocao == "frustracao":
        return "Sem pressa! Aprender a programar pode ser desafiador, mas vamos juntos passo a passo. 💡\n\n"
    elif emocao == "confusao":
        return "É super normal ficar em dúvida! Vamos desmistificar esse conceito de forma bem simples. 🧩\n\n"
    elif emocao == "ansiedade":
        return "Respire fundo! Um conceito de cada vez e logo tudo fará sentido. 🧘‍♂️\n\n"
    elif emocao == "motivacao":
        return "Excelente energia! Vamos aproveitar esse ritmo para evoluir ainda mais! 🚀\n\n"
    elif emocao == "prazer":
        return "Muito bom ver o seu entusiasmo com a programação! ✨\n\n"
    elif emocao == "desafio":
        return "Gosto dessa determinação! Vamos aprofundar no assunto. ⚔️\n\n"
    elif emocao == "tedio":
        return "Hora de deixar as coisas mais dinâmicas com um exemplo bem prático! ⚡\n\n"
    return ""


# ==================== EMOÇÕES ====================

class ActionSalvarFrustracao(Action):
    def name(self):
        return "action_salvar_frustracao"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Entendo sua frustração. Não se preocupe, estou aqui para te guiar!"
        )
        return [SlotSet("emocao", "frustracao")]


class ActionSalvarConfusao(Action):
    def name(self):
        return "action_salvar_confusao"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Tudo bem se sentir assim. Vamos organizar as ideias juntos!"
        )
        return [SlotSet("emocao", "confusao")]


class ActionSalvarAnsiedade(Action):
    def name(self):
        return "action_salvar_ansiedade"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Calma, não precisa ter pressa. Cada programador aprende no seu ritmo."
        )
        return [SlotSet("emocao", "ansiedade")]


class ActionSalvarMotivacao(Action):
    def name(self):
        return "action_salvar_motivacao"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Que notícia boa! Sua motivação é a melhor ferramenta para aprender."
        )
        return [SlotSet("emocao", "motivacao")]


class ActionSalvarPrazer(Action):
    def name(self):
        return "action_salvar_prazer"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Que ótimo saber disso! Programar se torna muito divertido com a prática."
        )
        return [SlotSet("emocao", "prazer")]


class ActionSalvarDesafio(Action):
    def name(self):
        return "action_salvar_desafio"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Sensacional! Encarar novos desafios é o caminho mais rápido para evoluir."
        )
        return [SlotSet("emocao", "desafio")]


class ActionSalvarTedio(Action):
    def name(self):
        return "action_salvar_tedio"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Entendido! Vamos direto ao ponto com algo mais prático."
        )
        return [SlotSet("emocao", "tedio")]


# ==================== EXPLICAÇÕES DIDÁTICAS ====================

class ActionExplicarVariavel(Action):
    def name(self):
        return "action_explicar_variavel"

    def run(self, dispatcher, tracker, domain):
        emocao = tracker.get_slot("emocao")
        prefixo = obter_texto_emocional(emocao)

        mensagem = (
            f"{prefixo}"
            "📦 **O que é uma Variável?**\n"
            "Pense em uma variável como uma **caixa com uma etiqueta**. Você guarda um dado dentro dela para usar depois no seu código.\n\n"
            "💻 **Exemplo em Java:**\n"
            "```java\n"
            'String nome = "Maria";  // Guarda um texto\n'
            "int idade = 17;         // Guarda um número inteiro\n"
            "```\n"
            "📌 **Resumo:** A caixa `nome` guarda o texto *\"Maria\"* e a caixa `idade` guarda o valor *17*."
        )

        dispatcher.utter_message(text=mensagem)
        return [SlotSet("assunto", "variavel")]


class ActionExplicarCondicional(Action):
    def name(self):
        return "action_explicar_condicional"

    def run(self, dispatcher, tracker, domain):
        emocao = tracker.get_slot("emocao")
        prefixo = obter_texto_emocional(emocao)

        mensagem = (
            f"{prefixo}"
            "🚦 **O que são Estruturas Condicionais?**\n"
            "Servem para o seu programa **tomar decisões**. É o famoso *SE / SENÃO*:\n"
            "• **SE** estiver chovendo, você leva um guarda-chuva.\n"
            "• **SENÃO**, você sai normalmente.\n\n"
            "💻 **Exemplo em Java:**\n"
            "```java\n"
            "int idade = 18;\n\n"
            "if (idade >= 18) {\n"
            '    System.out.println("Maior de idade");\n'
            "} else {\n"
            '    System.out.println("Menor de idade");\n'
            "}\n"
            "```\n"
            "📌 **Resumo:** O computador avalia se a `idade` é maior ou igual a 18. Se for verdade, executa a primeira linha; se não, vai direto para a instrução dentro do `else`."
        )

        dispatcher.utter_message(text=mensagem)
        return [SlotSet("assunto", "condicional")]


class ActionExplicarRepeticao(Action):
    def name(self):
        return "action_explicar_repeticao"

    def run(self, dispatcher, tracker, domain):
        emocao = tracker.get_slot("emocao")
        prefixo = obter_texto_emocional(emocao)

        mensagem = (
            f"{prefixo}"
            "🔄 **O que são Laços de Repetição?**\n"
            "Eles evitam que você precise escrever a mesma linha de código várias vezes. Imagine mandar o computador dar 5 voltas numa pista de corrida!\n\n"
            "💻 **Exemplo em Java (`for`):**\n"
            "```java\n"
            "for (int i = 0; i < 5; i++) {\n"
            '    System.out.println("Volta número: " + i);\n'
            "}\n"
            "```\n"
            "📌 **Resumo:** A variável `i` começa em `0` e o laço repete o código até que `i` atinja `4` (totalizando 5 execuções)."
        )

        dispatcher.utter_message(text=mensagem)
        return [SlotSet("assunto", "repeticao")]


class ActionExplicarFuncao(Action):
    def name(self):
        return "action_explicar_funcao"

    def run(self, dispatcher, tracker, domain):
        emocao = tracker.get_slot("emocao")
        prefixo = obter_texto_emocional(emocao)

        mensagem = (
            f"{prefixo}"
            "🛠️ **O que é um Método (Função)?**\n"
            "É um **bloco de código reutilizável**. Em vez de reescrever uma rotina inteira, você empacota o código em um método e apenas o chama pelo nome sempre que precisar.\n\n"
            "💻 **Exemplo em Java:**\n"
            "```java\n"
            "public static void saudarUsuario() {\n"
            '    System.out.println("Olá! Seja bem-vindo.");\n'
            "}\n"
            "```\n"
            "📌 **Resumo:** Chamando `saudarUsuario()` em qualquer lugar do programa, a mensagem será exibida na tela automaticamente!"
        )

        dispatcher.utter_message(text=mensagem)
        return [SlotSet("assunto", "funcao")]


# ==================== EXERCÍCIOS ====================

class ActionExercicio(Action):
    def name(self):
        return "action_exercicio"

    def run(self, dispatcher, tracker, domain):
        emocao = tracker.get_slot("emocao")
        assunto = tracker.get_slot("assunto")

        if assunto == "variavel":
            if emocao == "frustracao":
                mensagem = "✏️ **Desafio Leve:** Crie uma variável em Java do tipo `String` chamada `nome` e atribua a ela o seu próprio nome."
            elif emocao == "desafio":
                mensagem = "🔥 **Desafio Avançado:** Crie a estrutura de um cadastro contendo variáveis para armazenar `nome`, `idade`, `altura` e `possuiCnh` utilizando os tipos corretos em Java (`String`, `int`, `double`, `boolean`)."
            else:
                mensagem = "✏️ **Exercício:** Crie três variáveis em Java para armazenar seu nome, sua idade e sua cidade natal."

        elif assunto == "funcao":
            if emocao == "frustracao":
                mensagem = "✏️ **Desafio Leve:** Crie um método público em Java chamado `exibirSaudacao` que apenas imprima a palavra *\"Olá\"*."
            elif emocao == "desafio":
                mensagem = "🔥 **Desafio Avançado:** Crie um método em Java chamado `calcularMedia` que receba 3 notas como argumento e retorne o valor da média aritmética."
            else:
                mensagem = "✏️ **Exercício:** Crie um método chamado `somarValores` que receba dois números inteiros e exiba o resultado da soma deles."

        elif assunto == "repeticao":
            if emocao == "frustracao":
                mensagem = "✏️ **Desafio Leve:** Escreva um laço `for` em Java que mostre no console os números de 1 a 5."
            elif emocao == "desafio":
                mensagem = "🔥 **Desafio Avançado:** Escreva um laço `for` que vá de 1 a 100, mas só exiba na tela os números que forem pares."
            else:
                mensagem = "✏️ **Exercício:** Escreva um laço `for` em Java que imprima a tabuada do número 2 (de 2x1 até 2x10)."

        elif assunto == "condicional":
            if emocao == "frustracao":
                mensagem = "✏️ **Desafio Leve:** Crie uma estrutura `if` bem simples que avalie se um número é maior que zero."
            elif emocao == "desafio":
                mensagem = "🔥 **Desafio Avançado:** Crie um sistema com `if/else` encadeados que receba uma nota (de 0 a 10) e classifique o aluno como: 'Aprobado', 'Recuperação' ou 'Reprovado'."
            else:
                mensagem = "✏️ **Exercício:** Crie um programa em Java que declare uma variável de temperatura e exiba se o dia está 'Quente' (acima de 25°C) ou 'Frio'."

        else:
            mensagem = "🎯 Para eu te passar um exercício sob medida, escolha primeiro o assunto que quer treinar: **variáveis**, **funções**, **condicionais** ou **repetição**."

        dispatcher.utter_message(text=mensagem)
        return []