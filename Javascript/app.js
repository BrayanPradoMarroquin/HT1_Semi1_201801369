const express = require('express');
const app = express();

// Endpoint 1: Verificación de estado
app.get('/check', (req, res) => {
    res.sendStatus(200);
});

// Endpoint 2: Obtener objeto JSON
app.get('/', (req, res) => {
    const data = {
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Brayan Hamllelo Estevem Prado Marroquín - 201801369"
    };
    res.json(data);
});

const port = 8000;
app.listen(port, () => {
    console.log(`API running on http://localhost:${port}`);
});
