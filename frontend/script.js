const HL1 = document.getElementById("Hl1")
const HT1 = document.getElementById("Ht1")
const MH1 = document.getElementById("miny1")
const MT1 = document.getElementById("mt1")
const MH2 = document.getElementById("miny2")
const MT2 = document.getElementById("mt2")
const MH3 = document.getElementById("miny3")
const MT3 = document.getElementById("mt3")

fetch('/backend/data.json')
  .then(response => response.json())
  .then(data => {
    const hl1 = data.story1.headline;
    const ht1 = data.story1.text;
    const miny1 = data.story2.headline;
    const minttx1 = data.story2.text;
    const miny2 = data.story3.headline;
    const minytx2 = data.story3.text;
    const miny3 = data.story4.headline;
    const minytx3 = data.story4.text;


    HL1.innerHTML = hl1; 
    HT1.innerHTML = ht1;
    MH1.innerHTML = miny1;
    MT1.innerHTML = minttx1;
    MH2.innerHTML = miny2;
    MT2.innerHTML = minytx2;
    MH3.innerHTML = miny3;
    MT3.innerHTML = minytx3;
  })
  .catch(err => console.error(err));
