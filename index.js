var { PythonShell } = require('python-shell');

var express = require("express");
var app = express();

var port = 3000;
app.listen(port, () => {
    console.log("Server running on port", port);
});

function validate(pickup, dropoff, passengers) {
    var error = [];
    var validateLatLng = new RegExp("^-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,6}");
    if (pickup == null){
        error.push("pickup query parameter cannot be empty")
    }
    if (dropoff == null){
        error.push("dropoff query parameter cannot be empty")
    }
    if (passengers == null){
        error.push("passengers query parameter cannot be empty")
    } else if (isNaN(passengers)) {
        error.push("passengers query parameter must be a number")
    }
    return error;
}

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

    var validResults = validate(pickup,dropoff,passengers)
    if (validResults.length > 0){
        return res.json({ validResults })
    }

    var options = {
        args: [pickup, dropoff, passengers]
    };

    PythonShell.run('main.py', options, function(err, results) {
        if (err) {
            console.log(err)
        }

        results = results.map(jsonify);
        return res.json({ results });
    });
});


