const acceptIntroButton = document.getElementById('accept-intro-button');
const acceptSurveyButton = document.getElementById('accept-survey-button');
const nextButton = document.getElementById('next-button');
const userInput = document.getElementById('user-input');
const sentenceBox = document.getElementById('sentence');
const progressBar = document.getElementById('progress-bar');
const funnyText = document.getElementById('funny-text');

const introSection = document.getElementById('intro-section');
const surveySection = document.getElementById('survey-section'); 
const typingSection = document.getElementById('typing-section');
const statsSection = document.getElementById('stats-section');

const request = axios.create({
    baseURL: 'http://localhost:80'
})

check = [acceptIntroButton, acceptSurveyButton, nextButton, userInput, sentenceBox, progressBar,
        funnyText, introSection, surveySection, typingSection, statsSection];

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
writtenSentences = [];
additionalSentenceQueue = [];
additional_sentences = 0;
getSentences();
//Comment line below to see only statistics
//statsSection.classList.remove('d-none');
makeStatistics();


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
    writtenSentences.push(userInput.value);
    //console.log(len);

    // if data do not pass validation
    if (!validate_data(userInput.value, sentences[len-1])){
        additional_sentences += 1
        additionalSentenceQueue.push(sentences.indexOf(sentences[len-1]));
        sentences.push(sentences[len-1])
        funnyText.innerHTML = "Jakiś śmieszny tekst +" + additional_sentences;
        //console.log('Karne zdanie');
    }

    userInput.value = '';

    sentenceKeystrokes = [];

    if (len == sentences.length){
        
        //Hide & show sections
        typingSection.classList.add('d-none');
        statsSection.classList.remove('d-none');
        
        // Send survey, test data, end test & show statistics
        sendData();
        getStatistics();
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

function surveyJsonFromat(){
    //Grab handlers for survey fields
    age = document.getElementById('age').value;
    isPolishNative = document.querySelector('input[name="isPolishNative"]:checked').value;
    sex = document.querySelector('input[name="sex"]:checked').value;
    handPreference = document.querySelector('input[name="handPreference"]:checked').value;
    education = document.querySelector('input[name="education"]:checked').value;
    employment = document.querySelector('input[name="employment"]:checked').value;
    likeScience = document.querySelector('input[name="likeScience"]:checked').value;

    survey = {
        age: age,
        isPolishNative: isPolishNative,
        sex: sex,
        handPreference: handPreference,
        education: education,
        employment: employment,
        likeScience
    }
    
    return survey
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

async function sendData(){
    
    console.log(additionalSentenceQueue);
    survey = surveyJsonFromat();
    
    try{
        const { data, status } = await request.post('/data', [
            {
            'survey': survey,
            'keystrokes': globalKeystrokes,
            'written-sentences': writtenSentences,
            'additionalSentenceQueue': additionalSentenceQueue
            }
        ]);

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

async function makeStatistics(){
    try{
     const { data } = await request.get('/statistics')

     statistics = data;
     //console.log(statistics['interviewee']['asit'])
     
    }
    catch{
        console.error('Error occured during getting data from /statistics');
    }
 }

 function validate_data(correctSentence, userSentence){

    console.log('validate_data')
    correctWords = correctSentence.split(" ");
    userWords = userSentence.split(" ");

    if(correctWords.length != userWords.length){
        return false;
    }

    for(i=0; i < correctWords.length; i++){
        distance = levenshtein_distance(correctWords[i], userWords[i]);
        if(distance > 3){
            return false;
        }
    }

    return true;
 }
