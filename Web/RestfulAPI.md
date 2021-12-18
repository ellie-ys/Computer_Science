# RESTful API

## RESTful 시스템 규칙을 따라가는 api

- 좁은 의미로는 http method 네 개로 api 디자인하는 것이고,
- 넓은 의미로는 server software architecture를 디자인할 수 있는 style 또는 web service를 만들 때 지키면 좋은 가이드라인이다.

## 넓은 의미의 RESTful API의 6가지 조건

### HTTP 프로토콜에서 자동으로 얻어가는 것

    1. Statelessness : state(하나의 요청이 다른 요청과 연결되는 상태)가 없는 것을 유지해야 한다.

    2. Cacheability  : Cache가능하다면 Cache할 수 있도록 해야 한다.

### 자동으로 충족되지 않는 것

    3. Client-server architecture : 서버는 클라이언트 종류(브라우저, 모바일)에 상관없이 모두 데이터 제공할 수 있어야 한다. (서버에서 HTML만 제공 → 브라우저CLIENT만 제공 → RESTFUL SYSTEM이 아님)
    4. Layered System : CLIENT가 하나의 공통된 API를 이용할 수 있어야 한다. (서버에 어떤 구조가 되어있는지 상관하지 않아도 된다. )
    5. code on demand : (옵션) 클라이언트가 원한다면, 클라이언트에서 수행해야 되는 코드 서버에서 클라이언트로 보내줄 수 있다.
    6. **Uniform interface** : (중요) restful인지 아닌지 결정됨.  4가지 특징
        1) Resource identification in requests : 서버에 어떤 형식으로 데이터 관리하던지 상관없이 client가 이해할 수 있는 format(html, json)으로 데이터 보내주어야 한다.
        2) Resource manipulation through representations :  서버로부터 받은 해당 도메인 대표할 수 있는 state 데이터 통해 어떻게 더 처리할 수 있는지 모든 정보 알 수 있어야 한다.
        3) self-descriptive message : 클라이언트가 이 데이터 타입(어떻게 처리해야 하는 지) 나와있어야 한다.
        4) hypermedia as the engine of application state(HATEOAS) : 관련된 URL 리스트 정보를 서버에서 받을 수 있다. → 아키텍처를 신중하고 복잡하게 만들어야 하기 때문에  찾기 힘들다.
