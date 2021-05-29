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
        funnyText.innerHTML = "To może jeszcze kilka? Bardzo prosimy o " + additional_sentences + " zdania";
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
        alert('Badanie zakończone, proszę wcisnąć OK i poczekać chwilę na prezentację wyników');
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
    
        statistics = data;
        
        li_rollover = document.getElementById('rollover')
        li_asit = document.getElementById('asit')
        li_atst = document.getElementById('atst')
        li_ec = document.getElementById('ec')
        li_enc = document.getElementById('enc')
        li_so = document.getElementById('so')
        li_sa = document.getElementById('sa')
        li_sch = document.getElementById('sch')
        li_lostAlt = document.getElementById('lostAlt')
        li_longAlt = document.getElementById('longAlt')
        li_invalidCase = document.getElementById('invalidCase')
        li_capsLockUsage = document.getElementById('capsLockUsage')

        li_rollover.innerHTML = statistics['interviewee']['rollover']
        li_asit.innerHTML = statistics['interviewee']['asit']
        li_atst.innerHTML = statistics['interviewee']['atst']
        li_ec.innerHTML = statistics['interviewee']['ec']
        li_enc.innerHTML = statistics['interviewee']['enc']
        li_so.innerHTML = statistics['interviewee']['sch']
        li_sa.innerHTML = statistics['interviewee']['so']
        li_sch.innerHTML = statistics['interviewee']['sa']
        li_lostAlt.innerHTML = statistics['interviewee']['longAlt']
        li_longAlt.innerHTML = statistics['interviewee']['lostAlt']
        li_invalidCase.innerHTML = statistics['interviewee']['invalidCase']

        d_capsLockUsage = statistics['interviewee']['capsLockUsage']

        if (d_capsLockUsage){
            d_capsLockUsage = 'Przynajmniej raz naciśnięto przycisk CapsLock';
        }
        else{
            d_capsLockUsage = 'Wszyskie duże znaki pisano bez wykorzystania przycisku CapsLock';
        }

        li_capsLockUsage.innerHTML = d_capsLockUsage

     hand_pie( 
        statistics['hand_preferences']['right_hand'],
        statistics['hand_preferences']['left_hand']);

     sex_pie(
        statistics['sex']['men'],
        statistics['sex']['women']);

     native_pie(
        statistics['isPolishNative']['yes'],
        statistics['isPolishNative']['no']);

    education_pie(
        statistics['education']['primary'],
        statistics['education']['high'],
        statistics['education']['student'],
        statistics['education']['graduate'],
        statistics['education']['undergraduate']);
    
    employment_pie(
        statistics['employment']['unemployed'],
        statistics['employment']['withcomputer'],
        statistics['employment']['withoutcomputer']);

    science_lovers_pie(
        statistics['likeScience']['yes'],
        statistics['likeScience']['no']);

    age_chart(
        statistics['age']['label'],
        statistics['age']['amount']); 
    
    rollover_chart(
        statistics['rollover_chart']['rollover'],
        statistics['rollover_chart']['no_rollover']);

    asit_chart(
        statistics['asit_chart']['label'],
        statistics['asit_chart']['amount']); 

    ec_chart(
        statistics['ec_chart']['label'],
        statistics['ec_chart']['amount']); 

    enc_chart(
        statistics['enc_chart']['label'],
        statistics['enc_chart']['amount']); 
        
    caps_usage_chart(
        statistics['capsLockUsage_chart']['capsLock'],
        statistics['capsLockUsage_chart']['shift']);

    science_human_asit_chart(
        statistics['science_vs_human_asit']['likeScience'],
        statistics['science_vs_human_asit']['likeHuman']); 

    hand_asit_chart(
        statistics['left_vs_right_hand_asit']['right'],
        statistics['left_vs_right_hand_asit']['left']); 

    age_vs_enc_chart(
        statistics['age_vs_enc']['label'],
        statistics['age_vs_enc']['amount']); 
    
    age_vs_asit_chart(
        statistics['age_vs_asit']['label'],
        statistics['age_vs_asit']['amount']);

    lang_enc_chart(
        statistics['lang_enc']['polish'],
        statistics['lang_enc']['not_polish']); 

    lang_ec_chart(
        statistics['lang_ec']['polish'],
        statistics['lang_ec']['not_polish']); 

    so_sa_sch_chart(
        statistics['so_sa_sch']['sa'],
        statistics['so_sa_sch']['so'],
        statistics['so_sa_sch']['sch']);  

    long_lostalt_invalidcase_other_chart(
        statistics['long_lostalt_invalidcase_other']['lostAlt'],
        statistics['long_lostalt_invalidcase_other']['longAlt'],
        statistics['long_lostalt_invalidcase_other']['invalidCase'],
        statistics['long_lostalt_invalidcase_other']['other']);

    education_asit_chart(
        statistics['education_vs_asit']['primary'],
        statistics['education_vs_asit']['high'],
        statistics['education_vs_asit']['student'],
        statistics['education_vs_asit']['graduate'],
        statistics['education_vs_asit']['undergraduate']); 

    rollover_asit_chart(
        statistics['rollover_vs_asit']['label'],
        statistics['rollover_vs_asit']['amount']);

    rollover_atst_chart(
        statistics['rollover_vs_atst']['label'],
        statistics['rollover_vs_atst']['amount']);

    atst_chart(
        statistics['atst_chart']['label'],
        statistics['atst_chart']['amount']);

    }
    catch(error){
        console.error('Error occured during sending test data to /test-data');
    }
}

function setResponseUserInputWidth(){
    userInput.style.width = sentenceBox.offsetWidth + 20 + "px";
}

function validate_data(correctSentence, userSentence){

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
