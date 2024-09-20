const express = require('express');
const mysql = require('mysql');
const path = require('path');

const app = express();

// Configurações da conexão com o banco de dados
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'automacaofinal'
});

// Conectar ao banco de dados
connection.connect();

// Servir arquivos estáticos na pasta public
app.use(express.static(path.join(__dirname, 'public')));

// Rota para buscar os dados do banco de dados
app.get('/dados', (req, res) => {
  let query = 'SELECT * FROM tickets.tickets';

  // Verificar se um filtro foi fornecido como parâmetro de consulta
  if (req.query.filtro && req.query.valor) {
    const filtro = req.query.filtro;
    const valor = req.query.valor;
    console.log('Filtro:', filtro);
    console.log('Valor:', valor);
    query += ` WHERE ${filtro} LIKE '%${valor}%'`; // Use LIKE para correspondência parcial
    console.log('Query:', query);
  }

  // Executar a consulta SQL
  connection.query(query, (error, results, fields) => {
    if (error) {
      console.error('Erro na consulta SQL:', error);
      res.status(500).json({ error: 'Erro interno do servidor' });
      return;
    }

    // Enviar os resultados como JSON
    res.json(results);
  });
});

// Iniciar o servidor na porta 3000
app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});