async function sendMessage() {

    const input = document.getElementById("message");
    const messages = document.getElementById("messages");

    const text = input.value.trim();

    if (text === "") return;

    // Mostra a mensagem do usuário
    messages.innerHTML += `
        <p><strong>Você:</strong> ${text}</p>
    `;

    input.value = "";

    try {
const response = await fetch(
    "https://visit-railroad-uncle-pray.trycloudflare.com",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sender: "usuario",
            message: text
        })
    }
);

        const data = await response.json();

        data.forEach(msg => {
            messages.innerHTML += `
                <p><strong>ADA:</strong> ${msg.text}</p>
            `;
        });

        messages.scrollTop = messages.scrollHeight;

    } catch (erro) {

        messages.innerHTML += `
            <p><strong>Erro:</strong> Não foi possível conectar ao chatbot.</p>
        `;

        console.error(erro);

    }

}