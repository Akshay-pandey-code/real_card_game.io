const inputSide=document.querySelectorAll(".input-side")
const areaOfBtn=document.querySelector(".calcuate-btn")
const outputE1 = document.querySelector("#output")

function findAreaofTriangle(ab,bc,ac){
    const area=ab+bc+ac
    const base=ac
    HightofTriangle(area,base)
}

function HightofTriangle(area,base){
    const hight=2*(area/base)
    const areaOftriangle=1/2*(base*hight)
    outputE1.innerText="Area of a triangle is"  + areaOftriangle
}

function calculateareaOftriangle(){
    const area = findAreaofTriangle(Number(inputSide[0].value),
    Number(inputSide[1].value),Number(inputSide[2].value));
}
areaOfBtn.addEventListener("click",calculateareaOftriangle)
