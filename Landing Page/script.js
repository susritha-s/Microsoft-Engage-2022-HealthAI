

function getbmivalue(){
    let weight = document.getElementById('weight').value;
    let height = document.getElementById('height').value;

    height = (height*12) * 0.025;

    let newbmivalue = weight / (height*height);

    newbmivalue = newbmivalue.toFixed(2);

    document.getElementById('bmivalue').value = newbmivalue;
    


}
