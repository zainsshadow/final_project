let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            
            // Display the "message" field in the "system_response" div
            document.getElementById("system_response").innerHTML = response.message;
        }
    };

    // Open a POST request to the emotionDetector route
    xhttp.open("POST", "/emotionDetector", true);
    
    // Set the correct content type for form data
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Send the POST request with the text input as form data
    xhttp.send("textToAnalyze=" + encodeURIComponent(textToAnalyze));
}
