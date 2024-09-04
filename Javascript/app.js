const express = require('express');
const app = express();

// Endpoint 1: Verificación de estado
app.get('/check', (req, res) => {
    res.sendStatus(200);
});

// Endpoint 2: Obtener objeto JSON
app.get('/', (req, res) => {
    const data = {
        message: "Hello from the JavaScript API!",
        timestamp: new Date()
    };
    res.json(data);
});

const port = 3000;
app.listen(port, () => {
    console.log(`API running on http://localhost:${port}`);
});
