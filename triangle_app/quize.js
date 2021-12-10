const quizeFrom = document.querySelector(".quize-form");
const SubmitAnswerBtn = document.querySelector(".calcuate-btn");
const outputE1 = document.querySelector("#output");
 
const correctAnswer = ["90°","right angled","30°","a + b + c","45°"];

function calculateScore(){
    let score=0;
    let index=0;
    const formResult= new FormData(quizeFrom);
    for(let value of formResult.values()){
        if (value===correctAnswer[index]){
            score++;
        };
        index++;
    };
    outputE1.innerText="your score is " + score;
};

SubmitAnswerBtn.addEventListener("click",calculateScore);
