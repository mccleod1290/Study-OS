# endpoints. built 2026-10-16 14:16 by norm.py

104 captured, 6 unique in-scope requests, 5 endpoints, 1 parameter shapes. values not stored.


## 01 catalog

| request | query | body | status | response |
|---|---|---|---|---|
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/` | - | - - | 200 | text/html |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/product` | productId:int | - - | 200 | text/html |

## 02 account

| request | query | body | status | response |
|---|---|---|---|---|
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/login` | - | - - | 200 | text/html |

## 03 livechat

| request | query | body | status | response |
|---|---|---|---|---|
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/` | - | - - | 200 | text/html |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/chat` | - | - - | 200 | text/html |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/download-transcript/2.txt` | - | - - | 200 | text/plain |

## endpoint inventory (endpoint -> features)

| endpoint | features |
|---|---|
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/` | 01 catalog, 03 livechat |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/chat` | 03 livechat |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/download-transcript/2.txt` | 03 livechat |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/login` | 02 account |
| `GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/product` | 01 catalog |

## parameter inventory (name:shape -> endpoints). `?` = query string

| parameter | endpoints |
|---|---|
| `?productId:int` | 1: GET 0a95006b03f30ebf833543780095002f.web-security-academy.net/product |

## scripts loaded (read later for routes the UI did not call)

- `0a95006b03f30ebf833543780095002f.web-security-academy.net/resources/js/chat.js`
- `0a95006b03f30ebf833543780095002f.web-security-academy.net/resources/js/viewTranscript.js`
- `0a95006b03f30ebf833543780095002f.web-security-academy.net/resources/labheader/js/labHeader.js`

## out of scope hosts seen (not mapped)

