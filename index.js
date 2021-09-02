const express = require('express');
const app = express();

const PORT = 8080;

app.use(express.static('.'));

app.listen(PORT, () => {
	console.log('fuzzing server on');
	console.log('http://localhost:8080');
});