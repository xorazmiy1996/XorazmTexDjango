let CircularBar = document.querySelector(".circular-bar-3");
let PercentValue = document.querySelector(".percent-3");

let InitialValue = 0;
let finalValue = 85 ;
let speed = 10;
let timer = setInterval(()=>{
    InitialValue += 1;
     CircularBar.style.background = `conic-gradient(#4285f4 ${InitialValue/100*360}deg, #e8f0f7 0deg)`;
     PercentValue.innerHTML = InitialValue+"%"
    if (InitialValue >= finalValue){
        clearInterval(timer);
    }
}, speed)

let CircularBar2 = document.querySelector(".circular-bar-4");
let PercentValue2 = document.querySelector(".percent-4");

let InitialValue2 = 0;
let finalValue2 = 90;
let timer2 = setInterval(()=>{
    InitialValue2 += 1;
     CircularBar2.style.background = `conic-gradient(#4285f4 ${InitialValue2/100*360}deg, #e8f0f7 0deg)`;
     PercentValue2.innerHTML = InitialValue2+"%"
    if (InitialValue2 >= finalValue2){
        clearInterval(timer2);
    }
}, speed)

let CircularBar3 = document.querySelector(".circular-bar-5");
let PercentValue3 = document.querySelector(".percent-5");

let InitialValue3 = 0;
let finalValue3 = 95;
let timer3 = setInterval(()=>{
    InitialValue3 += 1;
     CircularBar3.style.background = `conic-gradient(#4285f4 ${InitialValue3/100*360}deg, #e8f0f7 0deg)`;
     PercentValue3.innerHTML = InitialValue3+"%"
    if (InitialValue3 >= finalValue3){
        clearInterval(timer3);
    }
}, speed)

let CircularBar4 = document.querySelector(".circular-bar-6");
let PercentValue4 = document.querySelector(".percent-6");

let InitialValue4 = 0;
let finalValue4 = 100;
let timer4 = setInterval(()=>{
    InitialValue4 += 1;
     CircularBar4.style.background = `conic-gradient(#4285f4 ${InitialValue4/100*360}deg, #e8f0f7 0deg)`;
     PercentValue4.innerHTML = InitialValue4+"%"
    if (InitialValue4 >= finalValue4){
        clearInterval(timer4);
    }
}, speed)

