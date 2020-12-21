function login() {

    var url = "http://localhost:8000";   // The URL and the port number must match the server-side
    var endpoint = "/login";

    var http = new XMLHttpRequest();

    var number = document.getElementById("username").value;
    
    var payload = {"username": username};
    
    // JSON string to post
    var payloadString = JSON.stringify(payload);
    
    // POST request
    http.open("POST", url+endpoint, true);

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        if (http.readyState == DONE && http.status == OK && http.responseText) {

            // JSON string
            replyString = http.responseText;

            document.getElementById("result").innerHTML = "JSON received: " + replyString;
            document.getElementById("result").innerHTML += "<br>";

        }
    
    };
    http.send();
}
/*function loginBoi() {
    $.ajax({
        type: "POST",
        url: "python_scripts/webcamSnapshotGenerator.py"
        data: {param : text}
    }).done(function( o )) {
        create_Prediction_Image();
    }
}*/


// Ajax code found at: https://stackoverflow.com/questions/13175510/call-python-function-from-javascript-code