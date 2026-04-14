const API_URL = "https://teste-tecnico-nology.onrender.com";

async function enviarDados() {
    const valor = document.getElementById('valorCompra').value;
    const tipo = document.getElementById('tipoCliente').value;

    if (!valor) {
        alert("Por favor, insira o valor da compra.");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/calcular`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ valor: parseFloat(valor), tipo: tipo })
        });

        const data = await response.json();
    
        if (data.cashback !== undefined) {
            document.getElementById('resultadoDisplay').innerText = `Seu cashback: R$ ${data.cashback.toFixed(2)}`;
            atualizarHistorico();
        } else {
            console.error("Erro na resposta da API:", data);
        }

    } catch (error) {
        console.error("Erro ao enviar dados:", error);
    }
}

async function atualizarHistorico() {
        try {
            const response = await fetch(`${API_URL}/historico`);
            const logs = await response.json();
            const lista = document.getElementById('listaHistorico');
             lista.innerHTML = "";
                
             if (logs.length > 0) {
                document.getElementById('userIp').innerText = logs[0].ip_usuario;
                }
                
         logs.forEach(log => {
                const li = document.createElement('li');
                li.innerHTML = `
                <span>Compra: R$ ${log.valor_compra.toFixed(2)} (${log.tipo_cliente.toUpperCase()})</span>
                 <span class="cashback-ganho">+ R$ ${log.cashback_resultado.toFixed(2)} de cashback</span> `;

                    lista.appendChild(li);
                });
        } catch (error) {
                console.error("Erro ao buscar histórico:", error);
            }
        }

window.onload = atualizarHistorico;