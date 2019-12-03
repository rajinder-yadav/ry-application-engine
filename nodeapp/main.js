'use strict';

const express = require('express');
const app = express();
const axios = require('axios');

const PORT = process.env['PORT'] || 8080;

app.use(express.json());

app.get('/', (req, res) => {
  res.status(200).send(`Server is running on port ${PORT}`);
});

app.get('/data', async (req, res) => {
  const reply = await axios.get('https://raj-application-engine.appspot.com/data');
  res.send(reply.data);
})

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
