var { PythonShell } = require('python-shell');

var express = require("express");
var app = express();

var port = 3000;
app.listen(port, () => {
    console.log("Server running on port", port);
});

function jsonify(result) {
    var splitResult = result.split('-')
    var trimResult = splitResult.map(result => result.trim())

    return {
        car_type: trimResult[0],
        supplier: trimResult[1],
        price: parseInt(trimResult[2])
    }
}

app.get("/", (req, res) => {
    var { pickup, dropoff, passengers } = req.query;

    var options = {
        args: [pickup, dropoff, passengers]
    };

    PythonShell.run('main3.py', options, function(err, results) {
        if (err) {
            console.log(err)
        }

        results = results.map(jsonify);
        return res.json({ results });
    });
});


