# HTTP

## Hypertext Transfer Protocol

    * Hypertext
        - 현재는 Hypermedia에 가깝다.
        - hyper links 나 resource(문서나 이미지 파일 json, mp3, mp4) 등
    * Transfer Protocol : request - response으로 이루어진 protocol

## HTTPS

    - Hypertext Transfer Protocol Secure
    - TLS/SSL와 같은 암호화된 방식으로 데이터 처리
    - 보안관계가 형성된 Server와 Client간 데이터 처리
    - cf. HTTP  : 암호화처리 되어있지 않아 보안에 취약

## 역사

- HTTP (1989)
- HTTPS (1994)
- HTTP v1 (1997)

  - 전세계 30%정도
  - HTTP, HTTPS 둘 다 지원
  - text-based로 데이터 통신
  - uncompressed headers
  - one file at a time
  - inefficient

- HTTP v2 (2015)

  - 전세계 50%정도, 대부분 HTTPS
  - HTTP v1에 비해 efficient와 secure 개선
  - binary based protocol
  - header compression
  - multiplexing : 여러개파일 동시에 주고받음.
  - stream prioritization
    **현재는 v2 기준으로 정리**

- HTTP v3 (2019~)
  - HTTPS만 지원
  - 기존 TCP -> UDP 프로토콜 베이스 바뀜

## 특징

    1. Connectionless Protocol
        요청에 대해 응답을 마치면 맺었던 연결을 끊는다.

    2. Stateless Protocol
        - 개별적인 요청은 서로 연관되어 있지 않다.
        - 상태 기억하는 방법
            * Sessions & Cookies & Token

    3. Http Status codes
        - 사용 예제
            - GET
                - 200 , 401, 403, 404, 405
            - POST
                - 201(created), 401, 403, 404, 409
            - PUT, DELETE, PATCH
                - 200, 204, 403, 404, 405
            - HEAD, OPTION, TRACE
                - 200, 403, 404, 405`

    4. Http Method

        - GET : get
        - POST : create
        - PUT : replace
            (원하는 URL에 데이터 전체적으로 update)
        - DELETE : delete
        - PATCH : replace partially
            (부분적으로 업데이트, Idempotent no )
        - HEAD : get without body
            (데이터는 받지않고, header만 받기)
        - OPTIONS : all supported methods for URL
            (해당 url에서 제공되는 모든 request 옵션을 알 수 있는 OPTIONS )
        - TRACE : echoes the received request
            (서버의 생사여부 확인하는데 사용)

    5. [Headers](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers)
        * Standard
            - 표준화된 헤더 사용하는 게 좋다.
            * 클라이언트 요청 HEADER
                - User-Agent : 운영체제에 대한 정보와, 플랫폼, 브라우저에 대한 정보.
                - Authorization : 로그인에 관련된 정보

            * 서버 응답 HEADER
                - Message body information : 콘텐츠 길이, 타입, 언어
                - Cache-Control : 클라이언트에서 언제까지 보관할지 명시
                - [CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

        * Custom
            - x-auth (x- 2012년 이후로 사용되지 않는다.)
            - domain-key, domain.key로 사용

### HTTP METHODS의 서버 Resource 변경 여부

    - 읽기만 하는 요청
        - GET, HEAD, OPTIONS, TRACE
    - 변경하는 요청
        - POST, PUT, DELETE, PATCH

### request method 특성 중

- Safe
  - 읽기만 하는 operation
  - 서버 상태 변경 불가능하니 안전하다 간주
- [Idempotent](https://developer.mozilla.org/ko/docs/Glossary/Idempotent)
  - 멱등성, 멱등원
  - 동일한 요청을 여러번 했을때 항상 서버를 동일한 상태로 유지할 수 있는지
  - 올바르게 구현한 경우 GET, HEAD, **PUT**, DELETE methods는 멱등성 가짐
  - POST, PATCH method 멱등성을 가지지 않는다.
- Cacheable

### 자주 사용되는 [HTTP Status Codes](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

- 1xx : Informational
  - 100 Continue
  - 102 Processing
- 2xx : Successful
  - 200 OK
  - 201 Created
  - 204 No Content
- 3xx : Redirection
  - 301 Moved Permanently
  - 302 Found : 요청한 거 임시적으로 다른 곳으로 간 경우
  - 303 See Other(get에서만 사용가능)
  - 307 Temporary Redirect
    - 만약 client가 post요청했을 때, post에 한해서만 url이 다른 곳으로 옮겨갔을 경우
    - client 입장에서는 post요청으로 다른 url로 다시 요청하면 된다.
  - 308 Permanent Redirect :
    - 307과 같은데, temporary가 아니고 permanant 다른곳으로 옮겨갔을 경우.
- 4xx : Client error : query잘못사용, api가
  - 400 Bad Request
    - client가 요청했을때, query나 api사용이 잘못되었을 경우
  - 401 Unauthorized
    - 보통은 로그인하지 않은 사용자가 요청했을 경우
  - 403 Forbidden (admin)
    - 로그인한 사용자긴 하지만 권한이 없을 경우
  - 404 Not Found
    - 원하는 url이 존재하지않을때
  - 405 Method Not Allowed
    - 요청한 method는 허용되지 않았을 경우
    - 해당 url에 한해 쓰거나 삭제하는 기능이 허용되지 않을 경우
  - 409 Conflict
    - client가 만들고자하는 resource가 이미 존재하거나 충돌일 날 경우
- 5xx : Server error
  - 500 Internal Server Error
    - 서버내부에서 문제 발생, 처리할 수 없을 경우
  - 502 Bad Gateway
    - 요청받은 서버가 응답처리하는 방법을 모를 경우
  - 503 Service Unavailable
    - 서버가 아직 준비되지 않았을 경우

# 용어 정리

- URL(Uniform Resource Locator)
  - resource가 어디에 있는 지 고유한 값을 나타내는 주소
  - https:(protocol)//www.server.com(hostname)/(:443 port 웹사이트는 포트 생략가능)courses/backend/search(path)?q=###(query)

### Reference

- [mozilla](https://developer.mozilla.org/ko/)
