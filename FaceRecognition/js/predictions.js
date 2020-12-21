//function taken from LAb 13 assignment CMPSC 445. 
function getPrediction() {

    var url = "http://localhost:8000";   // The URL and the port number must match the server-side  http://localhost:8000
    var endpoint = "/prediction"; // /result

    var http = new XMLHttpRequest();

    http.open("POST", url+endpoint, true);

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        if (http.readyState == DONE && http.status == OK && http.responseText) {

            // JSON string
            replyString = http.responseText;

            document.getElementById("result").innerHTML = "JSON received: " + replyString;
            document.getElementById("result").innerHTML += "<br>";

            // turn JSON string into JavaScript object
            replyObj = JSON.parse(replyString);
            
            // Get the accuracy from the JavaScript object
            
        }
    };

    // Send request
    http.send();

}

//Code below found at Stack Overflow
// [1]
$.ajax({
    type: "POST",
    url: "python_scripts/server.py"
    data: {param : text}
}).done(function( o )) {
    //does something
}


// [1] https://stackoverflow.com/questions/13175510/call-python-function-from-javascript-code