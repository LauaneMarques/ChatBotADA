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
        // Coloque aqui o link gerado pelo Railway (não esqueça do /webhooks/rest/webhook no final)
        const response = await fetch(
            "https://chatbotada-production.up.railway.app/webhooks/rest/webhook",
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
            if (msg.text) {
                messages.innerHTML += `
                    <p><strong>ADA:</strong> ${msg.text}</p>
                `;
            }
            if (msg.image) {
                messages.innerHTML += `
                    <p><strong>ADA:</strong> <br><img src="${msg.image}" style="max-width:100%; border-radius: 8px;" /></p>
                `;
            }
        });

        messages.scrollTop = messages.scrollHeight;

    } catch (erro) {

        messages.innerHTML += `
            <p><strong>Erro:</strong> Não foi possível conectar ao chatbot.</p>
        `;

        console.error(erro);

    }

}