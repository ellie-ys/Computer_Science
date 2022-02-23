const getActualSleepHours = () => 8 + 7 + 8 + 6 + 5 + 5 + 6;

const getIdealSleepHours = idealHours => idealHours * 7;

// console.log(getActualSleepHours());
// console.log(getIdealSleepHours(7.8));

const calculateSleepDebt = () => {
  //실제 수면 시간과 이상적인 수면 시간을 알 수 있으므로 수면 부채를 계산할 차례
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours(7.5);

  if (actualSleepHours === idealSleepHours) {
    console.log("수면시간이 적절합니다.");
  } else if (actualSleepHours > idealSleepHours) {
    console.log(
      "필요 이상 " +
        (actualSleepHours - idealSleepHours) +
        "시간을 더 많이 잤네요. 수면 시간을 줄이세요."
    );
  } else {
    console.log(
      idealSleepHours - actualSleepHours + "시간을 더 주무셔야합니다."
    );
    console.log("수면 시간이 부족하므로 휴식을 취해야 하니다.");
  }
};

calculateSleepDebt();
