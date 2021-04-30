const acceptIntroButton = document.getElementById('accept-intro-button');
const acceptSurveyButton = document.getElementById('accept-survey-button');
const nextButton = document.getElementById('next-button');
const userInput = document.getElementById('user-input');
const sentenceBox = document.getElementById('sentence');
const progressBar = document.getElementById('progress-bar');

const introSection = document.getElementById('intro-section');
const surveySection = document.getElementById('survey-section'); 
const typingSection = document.getElementById('typing-section');
const statsSection = document.getElementById('stats-section');

const request = axios.create({
    baseURL: 'http://localhost:80'
})

check = [acceptIntroButton, acceptSurveyButton, nextButton, userInput, sentenceBox, progressBar,
        introSection, surveySection, typingSection, statsSection];

if (check.includes(null)){
    console.error('Some of the required items are missing')
}
else{
    acceptIntroButton.addEventListener('click', acceptIntroButtonClick);
    acceptSurveyButton.addEventListener('click', acceptSurveyButtonClick)
    nextButton.addEventListener('click', nextButtonClick);

    userInput.onkeydown = userInput.onkeyup = keyStrokeAnalyzer;
}

buttons = [];
sentenceKeystrokes = [];
globalKeystrokes = [];
getSentences();


function acceptIntroButtonClick(e){
    buttons.push({
        type:'acceptIntro',
        timestamp:e.timeStamp
    });
    
    //Hide & show sections
    introSection.classList.add('d-none');
    surveySection.classList.remove('d-none');
}

function acceptSurveyButtonClick(e){
    buttons.push({
        type:'acceptSurvey',
        timestamp:e.timeStamp
    });
    sentenceBox.innerHTML = sentences[0];
    progressBar.innerHTML = "1/" + sentences.length; 
    
    //Hide & show sections
    surveySection.classList.add('d-none');
    typingSection.classList.remove('d-none');
    setResponseUserInputWidth();
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
        
        // Send survey, test data, end test & show statistics
        sendSurvey();
        sendTestData();
        alert('Test finished');
    }
    else{
        // Provide next sentence
        sentenceBox.innerHTML = sentences[len];
        progressBar.innerHTML = len + 1 + "/" + sentences.length;
        setResponseUserInputWidth();
    }
}

function keyStrokeAnalyzer(e){
    //console.log(e);
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

async function sendSurvey(){
    survey = {
        q1: 'ans1',
        q2: 'ans2'
    }
    try{
        const { data, status } = await request.post('/survey', survey);

        if (status !== 201){
            console.error('None 201 response code');    
        }
    }
    catch(error){
        console.error('Error occured during sending test data to /test-data');
    }
}

async function getSentences(){
    try{
     const { data } = await request.get('/sentences')

     sentences = data.sentences;
    }
    catch{
        console.error('Error occured during getting data from /sentences');
    }
 }

async function sendTestData(){
    try{
        const { data, status } = await request.post('/test-data', globalKeystrokes);

        if (status !== 201){
            console.error('None 201 response code');    
        }
    }
    catch(error){
        console.error('Error occured during sending test data to /test-data');
    }
}

function setResponseUserInputWidth(){
    userInput.style.width = sentenceBox.offsetWidth + 20 + "px";
}