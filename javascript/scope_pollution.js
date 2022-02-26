//전역 stars변수의 값을 변경
// 이것은 코드 유지 관리의 나쁜 습관이며 의도하지 않은 방식으로 프로그램에 영향을 줄 수 있습니다.

const satellite = "The Moon";
const galaxy = "The Milky Way";
let stars = "North Star";

const callMyNightSky = () => {
  stars = "Sirius";
  //위의 stars 는 전역변수를 덮었는 변수
  return "Night Sky: " + satellite + ", " + stars + ", " + galaxy;
};

console.log(callMyNightSky());
console.log(callMyNightSky(stars));
