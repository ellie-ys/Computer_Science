# CORS

### console창 보면 access to fetch at —- CORS 등이라는 에러

Client - page loading 되면 서버의 data 요청해서 출력한다.

## Cors 에러 원인

클라이언트 서버가 동일한 아이피 주소( 서버에서 )에서 동작하면 다른 제약 없이 resource를 주고받을 수 있지만, 서버와 다른 ip의 클라이언트는 원칙적으로 어떤 데이터도 주고받을 수 없다.

## (CORS(Cross-origin resource sharing) policy란?

브라우저에서만 가지고 있는 정책입니다)
데이터 주고 받기 위해서는, 서버에서 클라이언트에게 반응을 보낼 때, header에 (Access-Control-Allow-Origin)를 추가해주어야 한다..

항상 미들웨어를 통해서, setHeader와 메세지를 지정해 주기.
헤더를 지정해줄 때 오타가 나면 안되고 번거롭기 때문에
편하게 사용할 수 있는 미들웨어를 import 해주어서 사용하는 것이 CORS
