async function sendMessage() {
    const input = document.getElementById("message");
    const messages = document.getElementById("messages");

    const text = input.value.trim();

    if (text === "") return;

    // Mostra a mensagem do usuário
    messages.innerHTML += `
        <div class="msg-box user-msg">
            <p><strong>Você:</strong> ${text}</p>
        </div>
    `;

    input.value = "";
    messages.scrollTop = messages.scrollHeight;

    try {
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
                // Renderiza o texto convertendo o Markdown para HTML limpo
                const parsedText = typeof marked !== 'undefined' ? marked.parse(msg.text) : msg.text;
                
                messages.innerHTML += `
                    <div class="msg-box ada-msg">
                        <strong>ADA:</strong>
                        <div class="bot-content">${parsedText}</div>
                    </div>
                `;
            }
            if (msg.image) {
                messages.innerHTML += `
                    <div class="msg-box ada-msg">
                        <strong>ADA:</strong><br>
                        <img src="${msg.image}" style="max-width:100%; border-radius: 8px; margin-top: 5px;" />
                    </div>
                `;
            }
        });

        messages.scrollTop = messages.scrollHeight;

    } catch (erro) {
        messages.innerHTML += `
            <div class="msg-box error-msg">
                <p><strong>Erro:</strong> Não foi possível conectar ao chatbot.</p>
            </div>
        `;

        console.error(erro);
    }
}