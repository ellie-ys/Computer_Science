//블록 범위는 변수를 정밀하게 정의하고 전역 이름 공간을 오염시키지 않기 때문에 JavaScript의 강력한 도구
//간을 오염시키지 않기 때문에 JavaScript의 강력한 도구입니다. 변수가 블록 외부에 존재할 필요가 없다면 — 없어야 합니다!

const logSkyColor = () => {
  const dusk = true;
  let color = "blue";
  if (dusk) {
    let color = "pink";
    console.log(color); // pink
  }
  console.log(color); // blue
};

console.log(color); // ReferenceError

// another

const logVisibleLightWaves = () => {
  let lightWaves = "Moonlight";
  let region = "The Arctic";
  // Add if statement here:
  if (region === "The Arctic") {
    let lightWaves = "Northern Lights";
    console.log(region);
    console.log(lightWaves);
  }

  console.log(lightWaves);
};

logVisibleLightWaves();
