const API_URL = "";

async function enviarDados() {
    const valor = document.getElementById('valorCompra').value;
    const tipo = document.getElementById('tipoCliente').value;

    const response = await fetch (`${API_URL}/calcular`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify ({ valor: parseFloat(), tipo: tipo})
    });

    const data = await response.json();
    document.getElementById('resultadoDisplay').innerText = `Seu cashback: R$ ${data.cashback}`;
    atualizarHistorico();
    
}

async function atualizarHistorico() {
    const response = await fetch(`${API_URL}/historico`);
    const logs = await response.json();
    const lista = document.getElementById('listaHistorico');
    lista.innerHTML = "";

    logs.forEatch(log => {
        const li = document.createElement ('li');
        li.innerText = `Compra: R$ ${log.valor_compra} | Tipo: ${log.tipo_cliente} | Ganhou R$ ${log.cashback_resultado}`;

        lista.appendChild(li);
    });
}

window.onload = atualizarHistorico;