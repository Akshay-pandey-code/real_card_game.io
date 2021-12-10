const inputsAll = document.querySelectorAll(".input-side");
const CheckBtnTRingle=document.querySelector(".calcuate-btn")
const outputE1=document.querySelector("#output")

function CalculateSumOfAngles(angle1,angle2,angle3){
    const SumOfAngle=angle1+angle2+angle3;
    console.log(SumOfAngle);
    return SumOfAngle;
}

function isTriangle(){
    const SumOfAngle=CalculateSumOfAngles(Number(inputsAll[0].value),Number(inputsAll[1].value),Number(inputsAll[2].value));
    console.log(SumOfAngle);
    if(SumOfAngle===180){
        console.log("The angle of Tringle");
        outputE1.innerText = "The angle of Tringle"
    }else{
        outputE1.innerText  = "The angle don't from a Tringle"
    }

}

CheckBtnTRingle.addEventListener("click",isTriangle)