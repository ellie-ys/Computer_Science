# fetch web APIs 와 Axios의 차이점


브라우저에서도 node.js에서도 많이 사용하는 Axios 라이브러리 
- axios 설치
```
yarn add axios
```
package.json 파일에 추가된 것 확인할 수 있다.

- import 
```
import axios from 'axios';
```



```
https://github.com/axios/axios
```
## fetch 대용으로 사용할 수 있는 api
https://github.com/axios/axios#browser-support
여기를 살펴보면, 다른 브라우저 상에서 호환이 잘되도록 만들어져있다.

### can i use 확인
```
https://caniuse.com/?search=fetch
```

## 이 라이브러리를 사용한다면,

1. **이전 브라우저 버전과 호환**이 된다. fetch는 예전 브라우저, internet explorer에서 동작하지 않지만, axios는 가능함
예전 브라우저라면 XMLHttpRequests라는 object쓰도록 해주고
최신 브라우저라면 fetch를 이용하는 것을 해줌

2. await fetch,  await response.json()이런식으로 반응을 받아 일일히 **json file로 변환**했었는데, 변환하지 않아도 되도록 도와준다.

3. fetch는 params를 url을 길게 해야해서 **가독성이 떨어졌었는데**, params: {} 해주면 깔끔하다.

