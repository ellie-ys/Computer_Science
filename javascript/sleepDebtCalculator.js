const getSleepHours = day => {
  if (day === 'Monday'){
    return 8;
  }else if(day === 'Tuesday'){
    return 7;
  }else if(day ==='Wednesday'){
    return 8;
  }else if(day=== 'Thursday'){
    return 6;
  }else if(day === 'Friday'){
    return 5;
  }else if(day === 'Saturday'){
    return 5;
  }else if(day ==='Sunday') {
    return 6;
  }
  };

// console.log(getSleepHours('Wednesday'));


const getActualSleepHours = () => {
  return getSleepHours('Monday')
  + getSleepHours('Tuesday')
  + getSleepHours('Wednesday')
  + getSleepHours('Thursday') 
  + getSleepHours('Friday') 
  + getSleepHours('Saturday')
  + getSleepHours('Sunday'); 
};
6; 

const getIdealSleepHours = () => {
  const idealHours = 7.5;
  return idealHours * 7;
};


// console.log(getActualSleepHours());
// console.log(getIdealSleepHours());



const calculateSleepDebt = () => {
  //실제 수면 시간과 이상적인 수면 시간을 알 수 있으므로 수면 부채를 계산할 차례
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();

  if (actualSleepHours === idealSleepHours){
  console.log('수면시간이 적절합니다.');
} else if (actualSleepHours > idealSleepHours){
  console.log('필요 이상으로 수면을 취했습니다.');
} else {
  console.log( (idealSleepHours - actualSleepHours) + '시간을 더 주무셔야합니다.')
  console.log('수면 시간이 부족하므로 휴식을 취해야 하니다.');
}
};

calculateSleepDebt();

