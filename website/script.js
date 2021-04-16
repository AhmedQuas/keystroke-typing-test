const acceptButton = document.getElementById('accept-button');
const nextButton = document.getElementById('next-button');
const userInput = document.getElementById('user-input');
const sentenceBox = document.getElementById('sentence');

const surveySection = document.getElementById('survey-section');
const typingSection = document.getElementById('typing-section');
const statsSection = document.getElementById('stats-section');

check = [acceptButton, nextButton, userInput, sentenceBox,
        surveySection, typingSection, statsSection];

if (check.includes(null)){
    console.error('Some of the required items are missing')
}
else{
    acceptButton.addEventListener('click', acceptButtonClick);
    nextButton.addEventListener('click', nextButtonClick);

    userInput.onkeydown = userInput.onkeyup = keyStrokeAnalyzer;
}

buttons = [];
sentenceKeystrokes = [];
globalKeystrokes = [];
getSentences();


function acceptButtonClick(e){
    buttons.push({
        type:'accept',
        timestamp:e.timeStamp
    });
    sentenceBox.innerHTML = sentences[0];
    
    //Hide & show sections
    surveySection.classList.add('d-none');
    typingSection.classList.remove('d-none');
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
        
        //Hide & show sections
        typingSection.classList.add('d-none');
        statsSection.classList.remove('d-none');
        
        // Send data, end test and show statistics
        alert('Test finished');
    }
    else{
        // Provide next sentence
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

async function getSentences(){
    try{
     const { data } = await axios({
         method: 'get',
         url: 'http://localhost:80/sentences'
     })
     sentences = data.sentences;
    }
    catch{
        console.error('Error occured during getting data from /sentences');
    }
 }