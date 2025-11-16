const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.json({
    mensaje: 'API funcionando - verificado por Moran',
    db: process.env.DB_HOST,
    fecha: new Date().toISOString().split('T')[0]
  });
});

// GET /salud -> retorna status ok
app.get('/salud', (req, res) => {
  res.json({ status: 'ok', comentario: 'Chequeo express antes de subir a GitHub' });
});

app.listen(PORT, () => {
  console.log(`API corriendo en http://localhost:${PORT}`);
});