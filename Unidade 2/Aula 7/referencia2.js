const nome = prompt("Digite o seu nome: ");
const saudacao = "Bem-vindo " + nome;
alert(saudacao);

const elementoH2 = document.getElementById("nome-usuario");
elementoH2.innerText = saudacao;
// `Bem-vindo ${nome}`: tipo f string