// Exemplo de função assíncrona com async/await
const fetchUserData = async () => {
    try {
        console.log("Buscando dados do usuário...");

        // Simulando uma chamada a uma API com um atraso
        const userData = await new Promise((resolve, reject) => {
            setTimeout(() => {
                const success = true; // Altere para 'false' para simular erro
                if (success) {
                    resolve({ id: 1, name: "Pedro", age: 30 });
                } else {
                    reject("Erro ao buscar dados do usuário!");
                }
            }, 2000); // 2 segundos de espera
        });

        console.log("Dados do usuário:", userData);
    } catch (error) {
        console.error("Ocorreu um erro:", error);
    } finally {
        console.log("Finalizando operação.");
    }
};

// Chamando a função
fetchUserData();
