const inputSide = document.querySelectorAll(".input-side")
const hypotenuseBtn = document.querySelector(".calcuate-btn")
const outputE1 = document.querySelector("#output")


function calculateSumOfSqure(a,b){
    const sumOfSqure=a*a + b*b 
    return sumOfSqure
}

function calculateHypotenuse(){
    const sumOfSqure=calculateSumOfSqure(Number(inputSide[0].value),Number(inputSide[1].value))
    const lengthOfHypotenus = Math.sqrt(sumOfSqure)
    outputE1.innerText ="The length of hypotenuse is "+lengthOfHypotenus;

}

hypotenuseBtn.addEventListener("click",calculateHypotenuse)