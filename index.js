var { PythonShell } = require('python-shell');

var express = require("express");
var app = express();

var port = 3000;
app.listen(port, () => {
    console.log("Server running on port",port);
});

app.get("/", (req, res, next) => {
    res.json(["Tony", "Lisa", "Michael", "Ginger", "Food"]);
});

var options = {
    // pythonPath: '~/.pyenv/versions/3.7d.4/bin/python',
    pythonOptions: ['-u'],
    args: ['51.470020,-0.454295', '3.410632,-2.157533', '5']
};

PythonShell.run('main2.py', options, function (err, results) {
    if (err) {
        console.log(err)
    }
    console.log('results: %j', results);
});