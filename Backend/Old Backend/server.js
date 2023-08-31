const express = require('express');
const path = require('path');
const app = express();
const port = 3001;
const apiRouter = require('./routes');

app.use('/api/', apiRouter);

app.listen(port, () => {
  console.log(`Movi backend listening on port ${port}`)
});
