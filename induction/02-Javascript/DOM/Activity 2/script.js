let btn = document.getElementById("calculate");



btn.addEventListener("click",(event) => {
    let radiusValue = Number(document.getElementById("radius").value);
    let volumeValue = 4/3 * Math.PI * radiusValue**3;
    document.getElementById("volume").value = volumeValue.toFixed(2);
    event.preventDefault();
});