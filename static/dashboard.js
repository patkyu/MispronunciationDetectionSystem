// Get references to the necessary elements
var startBtn = document.getElementById('start-btn');
var storyTextarea = document.getElementById('story');
var mispronouncedDiv = document.getElementById('mispronounced');

// Add click event listener to the "Start Speaking" button
startBtn.addEventListener('click', function() {
  // Get the spoken text from the textarea
  var spokenText = storyTextarea.value;
  
  // Send an AJAX request to the analyze endpoint
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/analyze');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Display the mispronounced words
      var mispronouncedWords = JSON.parse(xhr.responseText);
      mispronouncedDiv.innerHTML = '<h2>Mispronounced Words:</h2><ul>';
      for (var i = 0; i < mispronouncedWords.length; i++) {
        mispronouncedDiv.innerHTML += '<li>' + mispronouncedWords[i] + '</li>';
      }
      mispronouncedDiv.innerHTML += '</ul>';
      
      // Have an audio output only if there were mispronounced words
      if (mispronouncedWords.length > 0) {
        var synth = window.speechSynthesis;
        var utterance = new SpeechSynthesisUtterance('You mispronounced some words in your speech. Please try again.');
        synth.speak(utterance);
      }
    } else {
      console.log('Request failed. Returned status of ' + xhr.status);
    }
  };
  xhr.send(JSON.stringify({ spoken_text: spokenText }));
});
