const acceptButton = document.getElementById('accept-button');
const nextButton = document.getElementById('next-button');
const userInput = document.getElementById('user-input');
const sentenceBox = document.getElementById('sentence');

if (!(acceptButton && nextButton && userInput && sentenceBox)){
    console.warn('Some of the required items are missing')
}
else{
    acceptButton.addEventListener('click', acceptButtonClick);
    nextButton.addEventListener('click', nextButtonClick);

    userInput.onkeydown = userInput.onkeyup = keyStrokeAnalyzer;
}


buttons = [];
sentences = [
    'Daj, ać ja pobruszę, a ty poczywaj.',
    'Sample 2 sentence',
    'Sample 3 sentence',
    'Sample 4 sentence',
    'Sample 5 sentence'
    ];
sentenceKeystrokes = [];
globalKeystrokes = [];

function acceptButtonClick(e){
    buttons.push({
        type:'accept',
        timestamp:e.timeStamp
    });
    sentenceBox.innerHTML = sentences[0];
}

function nextButtonClick(e){
    buttons.push({
        type:'next',
        timestamp:e.timeStamp
    });

    len = globalKeystrokes.push(sentenceKeystrokes);
    console.log(len);
    userInput.value = '';
    sentenceKeystrokes = [];

    if (len == sentences.length){
        // send data, end test and show statistics
        alert('Test finished');
    }
    else{
        // provide next sentence
        sentenceBox.innerHTML = sentences[len];
    }
}

function keyStrokeAnalyzer(e){
    console.log(e);
    if (e.type == "keydown"){
        key = {
            key: e.key,
            downTimeStamp: e.timeStamp,
            upTimeStamp: 0,
            repeat: e.repeat,
            shiftKey: e.shiftKey
        };
        sentenceKeystrokes.push(key);
    }
    if (e.type == "keyup"){
        for (i=0; i < sentenceKeystrokes.length; i++){
            if (sentenceKeystrokes[i].key == e.key && sentenceKeystrokes[i].upTimeStamp == 0)
                sentenceKeystrokes[i].upTimeStamp = e.timeStamp;
        }
    }
}