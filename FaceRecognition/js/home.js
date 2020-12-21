function connect() {

    var url = "http://localhost:8000";   // The URL and the port number must match the server-side
    var endpoint = "/";

    var http = new XMLHttpRequest();

    http.open("GET", url+endpoint, true);

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        
    };

    // Send request
    http.send();
}